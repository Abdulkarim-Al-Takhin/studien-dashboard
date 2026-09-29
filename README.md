# Studien-Dashboard

Dieses Projekt ist ein prototypisches Studien-Dashboard für das IU-Portfolio im Kurs „Objektorientierte und funktionale Programmierung mit Python“.

Das Dashboard überwacht den aktuellen Notendurchschnitt, den Studienfortschritt und die bereits erreichten ECTS-Punkte.

## Funktionen

- Anzeige der Studieninformationen
- Eintragen und Aktualisieren von Prüfungsleistungen
- Automatische Berechnung des aktuellen Notendurchschnitts
- Vergleich mit dem Zielnotendurchschnitt
- Berechnung der abgeschlossenen ECTS-Punkte
- Grafischer ECTS-Fortschrittsbalken
- Prüfung, ob der Studienfortschritt im Zeitplan liegt
- Speicherung der Prüfungsleistungen in einer JSON-Datei
- Validierung anhand eines festen Notenkatalogs
- Responsives dunkelgraues Webdesign

## Verwendete Technologien

- Python 3.13
- Flask 3.1.3
- HTML5
- CSS3
- JSON
- Git und GitHub

## Voraussetzungen

- Windows 10 oder Windows 11
- Python 3.13 
- Git
- Ein aktueller Webbrowser

## Installation unter Windows

1. Repository herunterladen:

```powershell
git clone https://github.com/Abdulkarim-Al-Takhin/studien-dashboard.git
```

2. In den Projektordner wechseln:

```powershell
cd studien-dashboard
```

3. Virtuelle Python-Umgebung erstellen:

```powershell
python -m venv .venv
```
4. Benötigte Python-Pakete installieren:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.txt
```

5. Anwendung starten:

```powershell
.\.venv\Scripts\python.exe app.py
```

6. Folgende Adresse im Browser öffnen:

```text
http://127.0.0.1:5000
```

## Projektstruktur

```text
studien-dashboard/
├── app.py
├── controllers.py
├── models.py
├── repository.py
├── services.py
├── study_plan.py
├── requirements.txt
├── data/
│   └── pruefungsleistungen.json
├── docs/
│   ├── gesamtarchitektur.puml
│   └── gesamtarchitektur.svg
├── static/
│   └── style.css
├── templates/
│   └── dashboard.html
└── tests/
    ├── test_app.py
    ├── test_models.py
    └── test_repository.py
```

## Datenspeicherung

Die Prüfungsleistungen werden dauerhaft in der Datei `data/pruefungsleistungen.json` gespeichert. Beim Start der Anwendung werden die vorhandenen Daten automatisch geladen. Neue Noten werden ergänzt und bereits vorhandene Noten aktualisiert.

## Bedienung

1. Im Notenformular ein Modul auswählen
2. Eine zulässige Note auswählen. Vorgesehen sind Zehntelnoten von `1,0` bis
   `4,0` sowie `5,0`. Die Noten `1,0` bis `4,0` gelten als bestanden.
3. Auf **Prüfungsleistung speichern** klicken.
4. Das Dashboard aktualisiert automatisch den Notendurchschnitt, die abgeschlossenen ECTS-Punkte und den Studienfortschritt.
5. Die Semesterbereiche können aufgeklappt werden, um die einzelnen Module und Prüfungsleistungen anzuzeigen.

## Autor

- Abdulkarim Al Takhin
- Studiengang: Angewandte Künstliche Intelligenz
- IU Internationale Hochschule

## Architektur

Der Prototyp trennt die Verantwortlichkeiten in fünf Bereiche:

- `models.py`: Domainklassen, Statuswerte und Notenvalidierung
- `study_plan.py`: Aufbau der Beispieldaten und des Studienplans
- `repository.py`: Laden und Speichern validierter Prüfungsleistungen
- `services.py`: Berechnungen und Anwendungslogik
- `controllers.py`: Verarbeitung der HTTP-Anfragen
- `app.py`: Programmeinstieg und Verbindung der Bestandteile
- `templates/` und `static/`: Darstellung und Gestaltung

## Automatisierte Tests

Die Domainlogik, Persistenz und Web-Routen werden mit der Python-
Standardbibliothek getestet:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```
