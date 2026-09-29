"""Erzeugt die Beispieldaten des Studien-Dashboards."""

from datetime import date

from models import Modul, ModulBelegung, Semester, Student, Studiengang


MODULE_NACH_SEMESTER = (
    (
        ("DLBDSEAIS01-01_D", "Artificial Intelligence", 5),
        ("DLBDSIPWP01_D", "Einführung in die Programmierung mit Python", 5),
        ("DLBBIMD01", "Mathematik: Analysis", 5),
        ("DLBWIRITT01", "Einführung in das wissenschaftliche Arbeiten für IT und Technik", 5),
        ("DLBDSOOFPP01_D", "Projekt: Objektorientierte und funktionale Programmierung mit Python", 5),
    ),
    (
        ("DLBBIM01", "Mathematik: Lineare Algebra", 5),
        ("DLBDSSPDS01_D", "Statistik - Wahrscheinlichkeit und deskriptive Statistik", 5),
        ("DLBDSSIS01_D", "Statistik - Induktive Statistik", 5),
        ("DLBDSCC01-01_D", "Cloud Computing", 5),
        ("DLBSEPCP01_D", "Projekt: Cloud Programming", 5),
    ),
    (
        ("DLBDSMLSL01_D", "Maschinelles Lernen - Supervised Learning", 5),
        ("DLBDSMLUSL01_D", "Maschinelles Lernen - Unsupervised Learning und Feature Engineering", 5),
        ("DLBDSNNDL01-01_D", "Neuronale Netze und Deep Learning", 5),
        ("DLBAIICV01_D", "Einführung in Computer Vision", 5),
        ("DLBAIPCV01_D", "Projekt: Computer Vision", 5),
    ),
    (
        ("DLBAIIRL01_D", "Einführung in das Reinforcement Learning", 5),
        ("DLBISIC01", "Einführung in Datenschutz und IT-Sicherheit", 5),
        ("DLBAIBEELAAI01_D", "Ethische und rechtliche Aspekte in der KI", 5),
        ("DLBAIINLP01_D", "Einführung in NLP", 5),
        ("DLBAIPNLP01_D", "Projekt: NLP", 5),
    ),
    (
        ("DLBAIPEAI01_D", "Projekt: Edge AI", 5),
        ("DLBAIBESEI01_D", "Seminar: Ethische Innovation", 5),
        ("WAHL-A", "Wahlpflichtmodule A", 5),
        ("WAHL-B1", "Wahlpflichtmodule B", 5),
        ("WAHL-B2", "Wahlpflichtmodule B", 5),
    ),
    (
        ("DLBDSME01_D", "Model Engineering", 5),
        ("BBAK01", "Bachelorarbeit", 9),
        ("BBAK02", "Kolloquium Bachelorarbeit", 1),
        ("WAHL-C1", "Wahlpflichtmodule C", 5),
        ("WAHL-C2", "Wahlpflichtmodule C", 5),
    ),
)


def erstelle_student_mit_studienplan():
    """Erzeugt den Studenten und den vollständigen Studienplan mit 180 ECTS."""
    studiengang = Studiengang(
        studienfach="Angewandte Künstliche Intelligenz",
        dauer_monate=36,
        gesamt_ects=180,
    )
    student = Student(
        name="Abdulkarim Al Takhin",
        matrikel_nr="anonymisiert",
        studiengang=studiengang,
        start_datum=date(2025, 12, 17),
        ziel_notendurchschnitt=2.0,
    )

    for semester_nummer, module in enumerate(MODULE_NACH_SEMESTER, start=1):
        semester = Semester(semester_nummer)
        for modul_code, name, ects in module:
            modul = Modul(modul_code, name, ects)
            semester.modul_liste.append(modul)
            student.modulbelegungen.append(ModulBelegung(modul))

        wahlmodul = Modul(
            f"WAHL-D-S{semester_nummer}",
            "Wahlpflichtbereich D",
            5,
        )
        semester.modul_liste.append(wahlmodul)
        student.modulbelegungen.append(ModulBelegung(wahlmodul))
        studiengang.semester_liste.append(semester)

    return student
