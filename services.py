"""Anwendungslogik zwischen Domain, Persistenz und Weboberfläche."""

import calendar
from datetime import date

from models import Pruefungsleistung


class DashboardService:
    def __init__(self, student, repository):
        self.student = student
        self.repository = repository

    def lade_pruefungsleistungen(self):
        """Überträgt gespeicherte Prüfungsleistungen in passende Belegungen."""
        for modul_code, pruefungsleistung in self.repository.laden().items():
            belegung = self.student.finde_modulbelegung(modul_code)
            if belegung is None:
                raise ValueError(f"Unbekannter Modulcode in der Datendatei: {modul_code}")
            belegung.pruefungsleistung_eintragen(pruefungsleistung.note)

    def pruefungsleistung_eintragen(self, modul_code, note):
        """Validiert, übernimmt und speichert eine Prüfungsleistung."""
        belegung = self.student.finde_modulbelegung(modul_code)
        if belegung is None:
            raise ValueError("Die ausgewählte Modulbelegung wurde nicht gefunden.")
        belegung.pruefungsleistung_eintragen(note)
        self.repository.speichern(self._vorhandene_pruefungsleistungen())

    def dashboard_daten(self, heute=None):
        """Bereitet alle Werte für die Darstellung des Dashboards auf."""
        heute = heute or date.today()
        noten = {}
        modulstatus = {}
        for belegung in self.student.modulbelegungen:
            modul_code = belegung.modul.modul_code
            modulstatus[modul_code] = belegung.status.value
            if belegung.pruefungsleistung is not None:
                noten[modul_code] = belegung.pruefungsleistung.note

        abgeschlossene_ects = self.student.berechne_abgeschlossene_ects()
        gesamt_ects = self.student.studiengang.gesamt_ects
        erfasste_gesamt_ects = self.student.studiengang.berechne_ects_aller_module()
        soll_ects = self._berechne_soll_ects(heute)
        ects_differenz = round(abgeschlossene_ects - soll_ects, 1)

        if ects_differenz > 5:
            fortschritt_status = "Du bist dem Zeitplan voraus."
        elif ects_differenz >= -5:
            fortschritt_status = "Du bist gut im Zeitplan."
        else:
            fortschritt_status = "Du bist hinter dem Zeitplan."

        return {
            "student": self.student,
            "noten": noten,
            "modulstatus": modulstatus,
            "durchschnitt": self.student.berechne_notendurchschnitt(),
            "notenziel_status": self.student.notenziel_status.value,
            "abgeschlossene_ects": abgeschlossene_ects,
            "ects_fortschritt_prozent": round(abgeschlossene_ects / gesamt_ects * 100, 1),
            "erfasste_gesamt_ects": erfasste_gesamt_ects,
            "studienplan_vollstaendig": erfasste_gesamt_ects == gesamt_ects,
            "soll_ects": soll_ects,
            "ects_differenz": ects_differenz,
            "fortschritt_status": fortschritt_status,
            "gueltige_noten": [float(note) for note in Pruefungsleistung.GUELTIGE_NOTEN],
        }

    def _vorhandene_pruefungsleistungen(self):
        return {
            belegung.modul.modul_code: belegung.pruefungsleistung
            for belegung in self.student.modulbelegungen
            if belegung.pruefungsleistung is not None
        }

    def _berechne_soll_ects(self, heute):
        start = self.student.start_datum
        monate = self.student.studiengang.dauer_monate
        ziel_monat_index = start.month - 1 + monate
        ziel_jahr = start.year + ziel_monat_index // 12
        ziel_monat = ziel_monat_index % 12 + 1
        ziel_tag = min(start.day, calendar.monthrange(ziel_jahr, ziel_monat)[1])
        ende = date(ziel_jahr, ziel_monat, ziel_tag)

        gesamte_tage = (ende - start).days
        vergangene_tage = min(max((heute - start).days, 0), gesamte_tage)
        zeitanteil = vergangene_tage / gesamte_tage
        return round(zeitanteil * self.student.studiengang.gesamt_ects, 1)
