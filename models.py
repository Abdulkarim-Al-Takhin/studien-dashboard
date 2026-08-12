
class Student:
    def __init__(self, name, matrikel_nr, id_student, studiengang, start_datum, ziel_notendurchschnitt):
        self.name = name
        self.matrikel_nr = matrikel_nr
        self.id_student = id_student
        self.start_datum = start_datum
        self.ziel_notendurchschnitt = ziel_notendurchschnitt
        self.studiengang = studiengang
        self.pruefungsleistungen = []

    def berechne_notendurchschnitt(self):
        """Berechnet den Durchschnitt aller vorhandenen Prüfungsnoten."""
        if len(self.pruefungsleistungen) == 0:
            return None

        noten = [
            pruefung.note for pruefung in self.pruefungsleistungen
        ]

        return round(sum(noten) / len(noten), 2)

    def ermittle_notenziel_status(self):
        """Vergleicht den aktuellen Durchschnitt mit dem persönlichen Notenziel."""
        durchschnitt = self.berechne_notendurchschnitt()

        if durchschnitt is None:
            return "Das Notenziel kann noch nicht bewertet werden."

        if durchschnitt <= self.ziel_notendurchschnitt:
            return "Du erreichst aktuell dein Notenziel"

        abweichung = round(durchschnitt - self.ziel_notendurchschnitt,2,)

        return ("Notenziel noch nicht erreicht. "f"Du liegst {abweichung} Notenpunkte über deinem Ziel.")

    def berechne_abgeschlossene_ects(self):
        """Berechnet die ECTS aller abgeschlossenen Module."""
        abgeschlossene_ects = 0

        for semester in self.studiengang.semester_liste:
            for modul in semester.modul_liste:
                if modul.status == "Abgeschlossen":
                     abgeschlossene_ects += modul.ects

        return abgeschlossene_ects

    def pruefungsleistung_speichern(self, modul, note):
        """Fügt eine Prüfungsleistung hinzu oder aktualisiert ihre Note."""
        for pruefung in self.pruefungsleistungen:
            if pruefung.modul.modul_id == modul.modul_id:
                pruefung.note = note
                modul.aktualisiere_status(note)
                return
        neue_pruefung = Pruefungsleistung(
            note=note,
            modul=modul,
        )

        self.pruefungsleistungen.append(neue_pruefung)
        modul.aktualisiere_status(note)

class Studiengang:
    def __init__(self, studienfach, dauer, gesamt_ects):
        self.studienfach = studienfach
        self.dauer = dauer
        self.gesamt_ects = gesamt_ects
        self.semester_liste = []

    def berechne_ects_aller_module(self):
        """Berechnet die Summe der ECTS aller eingetragenen Module."""
        erfasste_ects = 0

        for semester in self.semester_liste:
            for modul in semester.modul_liste:
                erfasste_ects += modul.ects

        return erfasste_ects

    def finde_modul(self, modul_id):
        """Sucht ein Modul anhand seiner eindeutigen Modul-ID."""
        for semester in self.semester_liste:
            for modul in semester.modul_liste:
                if modul.modul_id == modul_id:
                    return modul

        return None

class Semester:
    def __init__(self,semester_nr):
        self.semester_nr = semester_nr
        self.modul_liste = []

class Modul:
    def __init__(self, modul_id, name, ects, status):
        self.modul_id = modul_id
        self.name = name
        self.ects = ects
        self.status = status  #'Offen' oder 'Abgeschlossen'

    def aktualisiere_status(self, note):
        """Aktualisiert den Modulstatus anhand der Prüfungsnote."""
        if note <= 4.0:
            self.status = "Abgeschlossen"
        else:
            self.status = "Nicht bestanden"


class Pruefungsleistung:
    def __init__(self, note, modul):
        self.note = note
        self.modul = modul
