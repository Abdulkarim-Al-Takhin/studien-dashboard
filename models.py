"""Domainmodell des Studien-Dashboards."""

from decimal import Decimal, InvalidOperation
from enum import Enum


class Modulstatus(Enum):
    OFFEN = "Offen"
    ABGESCHLOSSEN = "Abgeschlossen"
    NICHT_BESTANDEN = "Nicht bestanden"


class NotenzielStatus(Enum):
    KEINE_NOTEN = "Keine Noten"
    ERREICHT = "Erreicht"
    NICHT_ERREICHT = "Nicht erreicht"


class Student:
    def __init__(self, name, matrikel_nr, studiengang, start_datum, ziel_notendurchschnitt):
        self.name = name
        self.matrikel_nr = matrikel_nr
        self.start_datum = start_datum
        self.ziel_notendurchschnitt = ziel_notendurchschnitt
        self.studiengang = studiengang
        self.modulbelegungen = []

    def berechne_notendurchschnitt(self):
        """Berechnet den Durchschnitt aller vorhandenen Prüfungsnoten."""
        noten = [
            belegung.pruefungsleistung.note
            for belegung in self.modulbelegungen
            if belegung.pruefungsleistung is not None
        ]
        if not noten:
            return None
        return round(sum(noten) / len(noten), 2)

    @property
    def notenziel_status(self):
        """Ermittelt den Status des persönlichen Notenziels."""
        durchschnitt = self.berechne_notendurchschnitt()
        if durchschnitt is None:
            return NotenzielStatus.KEINE_NOTEN
        if durchschnitt <= self.ziel_notendurchschnitt:
            return NotenzielStatus.ERREICHT
        return NotenzielStatus.NICHT_ERREICHT

    def berechne_abgeschlossene_ects(self):
        """Addiert die ECTS aller bestandenen Modulbelegungen."""
        return sum(
            belegung.modul.ects
            for belegung in self.modulbelegungen
            if belegung.status == Modulstatus.ABGESCHLOSSEN
        )

    def finde_modulbelegung(self, modul_code):
        """Gibt die Belegung zu einem Modulcode zurück."""
        return next(
            (
                belegung
                for belegung in self.modulbelegungen
                if belegung.modul.modul_code == modul_code
            ),
            None,
        )


class Studiengang:
    def __init__(self, studienfach, dauer_monate, gesamt_ects):
        self.studienfach = studienfach
        self.dauer_monate = dauer_monate
        self.gesamt_ects = gesamt_ects
        self.semester_liste = []

    def berechne_ects_aller_module(self):
        """Berechnet die Summe der ECTS aller eingetragenen Module."""
        return sum(
            modul.ects
            for semester in self.semester_liste
            for modul in semester.modul_liste
        )

    def finde_modul(self, modul_code):
        """Sucht ein Modul anhand seines eindeutigen Modulcodes."""
        for semester in self.semester_liste:
            for modul in semester.modul_liste:
                if modul.modul_code == modul_code:
                    return modul
        return None


class Semester:
    def __init__(self, semester_nummer):
        self.semester_nummer = semester_nummer
        self.modul_liste = []


class Modul:
    def __init__(self, modul_code, name, ects):
        self.modul_code = modul_code
        self.name = name
        self.ects = ects


class Pruefungsleistung:
    """Eine validierte und nach der Erzeugung unveränderliche Prüfungsnote."""

    GUELTIGE_NOTEN = tuple(
        Decimal(zehntel) / Decimal("10") for zehntel in range(10, 41)
    ) + (Decimal("5.0"),)
    BESTANDENE_NOTEN = GUELTIGE_NOTEN[:-1]

    def __init__(self, note):
        try:
            validierte_note = Decimal(str(note).replace(",", "."))
        except (InvalidOperation, ValueError):
            raise ValueError("Die eingegebene Note ist ungültig.") from None

        if validierte_note not in self.GUELTIGE_NOTEN:
            erlaubte_werte = ", ".join(
                str(wert).replace(".", ",") for wert in self.GUELTIGE_NOTEN
            )
            raise ValueError(f"Zulässige Noten sind: {erlaubte_werte}.")

        self.__note = validierte_note

    @property
    def note(self):
        """Gibt die validierte Note für Anzeige und Berechnungen zurück."""
        return float(self.__note)

    @property
    def bestanden(self):
        """Gibt an, ob die Note zum Katalog der bestandenen Noten gehört."""
        return self.__note in self.BESTANDENE_NOTEN


class ModulBelegung:
    def __init__(self, modul):
        self.modul = modul
        self.__pruefungsleistung = None

    @property
    def pruefungsleistung(self):
        """Gibt die aktuelle Prüfungsleistung zurück, sofern sie existiert."""
        return self.__pruefungsleistung

    @property
    def status(self):
        """Leitet den Modulstatus aus der aktuellen Prüfungsleistung ab."""
        if self.__pruefungsleistung is None:
            return Modulstatus.OFFEN
        if self.__pruefungsleistung.bestanden:
            return Modulstatus.ABGESCHLOSSEN
        return Modulstatus.NICHT_BESTANDEN

    def pruefungsleistung_eintragen(self, note):
        """Validiert eine Note und ersetzt die aktuelle Prüfungsleistung."""
        self.__pruefungsleistung = Pruefungsleistung(note)
