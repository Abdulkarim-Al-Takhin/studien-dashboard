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
- Responsives dunkelgraues Webdesign

## Verwendete Technologien

- Python 3.14
- Flask 3.1.3
- HTML5
- CSS3
- JSON
- Git und GitHub

## Voraussetzungen

- Windows 10 oder Windows 11
- Python 3.13 oder neuer
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
├── models.py
├── repository.py
├── requirements.txt
├── data/
│   └── pruefungsleistungen.json
├── static/
│   └── style.css
└── templates/
    └── dashboard.html
```

## Datenspeicherung

Die Prüfungsleistungen werden dauerhaft in der Datei `data/pruefungsleistungen.json` gespeichert. Beim Start der Anwendung werden die vorhandenen Daten automatisch geladen. Neue Noten werden ergänzt und bereits vorhandene Noten aktualisiert.

## Bedienung

1. Im Notenformular ein Modul auswählen
2. Eine Note zwischen `1,0` und `6,0` eingeben.
3. Auf **Prüfungsleistung speichern** klicken.
4. Das Dashboard aktualisiert automatisch den Notendurchschnitt, die abgeschlossenen ECTS-Punkte und den Studienfortschritt.
5. Die Semesterbereiche können aufgeklappt werden, um die einzelnen Module und Prüfungsleistungen anzuzeigen.

## Autor

- Abdulkarim Al Takhin
- Studiengang: Angewandte Künstliche Intelligenz
- IU Internationale Hochschule