#1. Imports

from datetime import date
from flask import Flask, redirect, render_template, request, url_for
from models import Student, Studiengang, Semester, Modul
from repository import PruefungsleistungRepository

#2. Flask erstellen

app = Flask(__name__)

# 3. Sämtliche Objekte erstellen

studiengang = Studiengang(
    studienfach="Angewandte Künstliche Intelligenz",
    dauer=6,
    gesamt_ects=180,
)

student = Student(
    name="Abdulkarim Al Takhin",
    matrikel_nr="anonymisiert",
    id_student=0,
    studiengang=studiengang,
    start_datum=date(2026, 1, 1),
    ziel_notendurchschnitt=2.0
)

semester_1 = Semester(semester_nr=1)
semester_2 = Semester(semester_nr=2)
semester_3 = Semester(semester_nr=3)
semester_4 = Semester(semester_nr=4)
semester_5 = Semester(semester_nr=5)
semester_6 = Semester(semester_nr=6)

studiengang.semester_liste.append(semester_1)
studiengang.semester_liste.append(semester_2)
studiengang.semester_liste.append(semester_3)
studiengang.semester_liste.append(semester_4)
studiengang.semester_liste.append(semester_5)
studiengang.semester_liste.append(semester_6)

modul_ai= Modul(
    modul_id="DLBDSEAIS01-01_D",
    name="Artificial Intelligence",
    ects=5,
    status="Offen"
)

modul_epp= Modul(
    modul_id="DLBDSIPWP01_D",
    name="Einführung in die Programmierung mit Python",
    ects=5,
    status="Offen"
)

modul_analysis= Modul(
    modul_id="DLBBIMD01",
    name="Mathematik: Analysis",
    ects=5,
    status="Offen"
)

modul_it_technik= Modul(
    modul_id="DLBWIRITT01",
    name="Einführung in das wissenschaftliche Arbeiten für IT und Technik",
    ects=5,
    status="Offen"
)

modul_ofpp= Modul(
    modul_id="DLBDSOOFPP01_D",
    name="Projekt: Objektorientierte und funktionale Programmierung mit Python",
    ects=5,
    status="Offen"
)

semester_1.modul_liste.append(modul_ai)
semester_1.modul_liste.append(modul_epp)
semester_1.modul_liste.append(modul_analysis)
semester_1.modul_liste.append(modul_it_technik)
semester_1.modul_liste.append(modul_ofpp)

modul_la= Modul(
    modul_id="DLBBIM01",
    name="Mathematik: Lineare Algebra",
    ects=5,
    status="Offen"
)

modul_swds= Modul(
    modul_id="DLBDSSPDS01_D",
    name="Statistik - Wahrscheinlichkeit und deskriptive Statistik",
    ects=5,
    status="Offen"
)

modul_is= Modul(
    modul_id="DLBDSSIS01_D",
    name="Statistik - Induktive Statistik",
    ects=5,
    status="Offen"
)

modul_cd= Modul(
    modul_id="DLBDSCC01-01_D",
    name="Cloud Computing",
    ects=5,
    status="Offen"
)

modul_pcd= Modul(
    modul_id="DLBSEPCP01_D",
    name="Projekt: Cloud Programming",
    ects=5,
    status="Offen"
)

semester_2.modul_liste.append(modul_la)
semester_2.modul_liste.append(modul_swds)
semester_2.modul_liste.append(modul_is)
semester_2.modul_liste.append(modul_cd)
semester_2.modul_liste.append(modul_pcd)

modul_ml_sl= Modul(
    modul_id="DLBDSMLSL01_D",
    name="Maschinelles Lernen - Supervised Learning",
    ects=5,
    status="Offen"
)

modul_ml_ulfe= Modul(
    modul_id="DLBDSMLUSL01_D",
    name="Maschinelles Lernen - Unsupervised Learning und Feature Engineering",
    ects=5,
    status="Offen"
)

modul_nndl= Modul(
    modul_id="DLBDSNNDL01-01_D",
    name="Neuronale Netze und Deep Learning",
    ects=5,
    status="Offen"
)

modul_ecv= Modul(
    modul_id="DLBAIICV01_D",
    name="Einführung in Computer Vision",
    ects=5,
    status="Offen"
)

modul_pcv= Modul(
    modul_id="DLBAIPCV01_D",
    name="Projekt: Computer Vision",
    ects=5,
    status="Offen"
)

semester_3.modul_liste.append(modul_ml_sl)
semester_3.modul_liste.append(modul_ml_ulfe)
semester_3.modul_liste.append(modul_nndl)
semester_3.modul_liste.append(modul_ecv)
semester_3.modul_liste.append(modul_pcv)

modul_erl= Modul(
    modul_id="DLBAIIRL01_D",
    name="Einführung in das Reinforcement Learning",
    ects=5,
    status="Offen"
)

modul_edi= Modul(
    modul_id="DLBISIC01",
    name="Einführung in Datenschutz und IT-Sicherheit",
    ects=5,
    status="Offen"
)

modul_era= Modul(
    modul_id="DLBAIBEELAAI01_D",
    name="Ethische und rechtliche Aspekte in der KI",
    ects=5,
    status="Offen"
)

modul_enlp= Modul(
    modul_id="DLBAIINLP01_D",
    name="Einführung in NLP",
    ects=5,
    status="Offen"
)

modul_pnlp= Modul(
    modul_id="DLBAIPNLP01_D",
    name="Projekt: NLP",
    ects=5,
    status="Offen"
)

semester_4.modul_liste.append(modul_erl)
semester_4.modul_liste.append(modul_edi)
semester_4.modul_liste.append(modul_era)
semester_4.modul_liste.append(modul_enlp)
semester_4.modul_liste.append(modul_pnlp)

modul_pea= Modul(
    modul_id="DLBAIPEAI01_D",
    name="Projekt: Edge AI",
    ects=5,
    status="Offen"
)

modul_sei= Modul(
    modul_id="DLBAIBESEI01_D",
    name="Seminar: Ethische Innovation",
    ects=5,
    status="Offen"
)

modul_wahl_a= Modul(
    modul_id="WAHL-A",
    name="Wahlpflichtmodule A",
    ects=5,
    status="Offen"
)

modul_wahl_b1= Modul(
    modul_id="WAHL-B1",
    name="Wahlpflichtmodule B",
    ects=5,
    status="Offen"
)

modul_wahl_b2= Modul(
    modul_id="WAHL-B2",
    name="Wahlpflichtmodule B",
    ects=5,
    status="Offen"
)

semester_5.modul_liste.append(modul_pea)
semester_5.modul_liste.append(modul_sei)
semester_5.modul_liste.append(modul_wahl_a)
semester_5.modul_liste.append(modul_wahl_b1)
semester_5.modul_liste.append(modul_wahl_b2)

modul_me= Modul(
    modul_id="DLBDSME01_D",
    name="Model Engineering",
    ects=5,
    status="Offen"
)

modul_ba= Modul(
    modul_id="BBAK01",
    name="Bachelorarbeit",
    ects=9,
    status="Offen"
)

modul_bak= Modul(
    modul_id="BBAK02",
    name="Kolloquium Bachelorarbeit",
    ects=1,
    status="Offen"
)

modul_wahl_c1= Modul(
    modul_id="WAHL-C1",
    name="Wahlpflichtmodule C",
    ects=5,
    status="Offen"
)

modul_wahl_c2= Modul(
    modul_id="WAHL-C2",
    name="Wahlpflichtmodule C",
    ects=5,
    status="Offen"
)

semester_6.modul_liste.append(modul_me)
semester_6.modul_liste.append(modul_ba)
semester_6.modul_liste.append(modul_bak)
semester_6.modul_liste.append(modul_wahl_c1)
semester_6.modul_liste.append(modul_wahl_c2)

# In jedem Semester gibt es einen Wahlpflichtbereich D mit 5 ECTS.
for semester in studiengang.semester_liste:
    modul_wahl_d = Modul(
        modul_id=f"WAHL-D-S{semester.semester_nr}",
        name="Wahlpflichtbereich D",
        ects=5,
        status="Offen"
    )
    semester.modul_liste.append(modul_wahl_d)

repository = PruefungsleistungRepository()

student.pruefungsleistungen = repository.laden(
    studiengang
)
@app.route("/pruefungsleistung/eintragen", methods=["POST"])
def pruefungsleistung_eintragen():
    modul_id = request.form["modul_id"]
    noten_text = request.form["note"].replace(",",".")

    try:
        note = float(noten_text)
    except ValueError:
        return "Die eingegebene Note ist ungültig.", 400

    if note <1.0 or note > 6.0:
        return "Die Note muss zwischen 1,0 und 6,0 liegen.", 400

    modul = studiengang.finde_modul(modul_id)

    if modul is None:
        return "Das ausgewählte Modul wurde nicht gefunden.", 404

    student.pruefungsleistung_speichern(
        modul,
        note,
    )

    repository.speichern(
        student.pruefungsleistungen
    )

    return redirect(url_for("dashboard"))

@app.route("/")
def dashboard():
    noten = {}

    for pruefung in student.pruefungsleistungen:
        noten[pruefung.modul.modul_id] = pruefung.note

    durchschnitt = student.berechne_notendurchschnitt()
    notenziel_status = student.ermittle_notenziel_status()

    abgeschlossene_ects = student.berechne_abgeschlossene_ects()

    ects_fortschritt_prozent = round(
        abgeschlossene_ects
        / student.studiengang.gesamt_ects
        * 100,
        1,
    )

    erfasste_gesamt_ects = (
        student.studiengang.berechne_ects_aller_module()
    )

    studienplan_vollstaendig = (
        erfasste_gesamt_ects
        == student.studiengang.gesamt_ects
    )

    heute = date.today()
    start_datum = student.start_datum
    end_datum = date(
        start_datum.year + 3,
        start_datum.month,
        start_datum.day
    )

    gesamte_studiendauer_tage = (end_datum - start_datum).days
    vergangene_tage = (heute - start_datum).days

    if vergangene_tage < 0:
        vergangene_tage = 0
    elif vergangene_tage > gesamte_studiendauer_tage:
        vergangene_tage = gesamte_studiendauer_tage

    zeitanteil = vergangene_tage / gesamte_studiendauer_tage

    soll_ects = (
            zeitanteil
            * student.studiengang.gesamt_ects
    )

    soll_ects = round(soll_ects, 1)

    ects_differenz = abgeschlossene_ects - soll_ects
    ects_differenz = round(ects_differenz, 1)

    if ects_differenz > 5:
        fortschritt_status = "Du bist dem Zeitplan voraus."
    elif ects_differenz >= -5:
        fortschritt_status = "Du bist gut im Zeitplan."
    else:
        fortschritt_status = "Du bist hinter dem Zeitplan."


    return render_template(
        "dashboard.html",
        student=student,
        noten=noten,
        durchschnitt=durchschnitt,
        notenziel_status=notenziel_status,
        abgeschlossene_ects=abgeschlossene_ects,
        ects_fortschritt_prozent=ects_fortschritt_prozent,
        erfasste_gesamt_ects=erfasste_gesamt_ects,
        studienplan_vollstaendig=studienplan_vollstaendig,
        soll_ects=soll_ects,
        ects_differenz=ects_differenz,
        fortschritt_status=fortschritt_status,
    )

if __name__ == "__main__":
    app.run(debug=True)
