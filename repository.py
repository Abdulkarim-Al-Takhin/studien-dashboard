"""Persistenzschicht für Prüfungsleistungen."""

import json
from pathlib import Path

from models import Pruefungsleistung


class PruefungsleistungRepository:
    """Speichert Prüfungsleistungen getrennt von der Anwendungslogik als JSON."""

    def __init__(self, dateipfad=None):
        self.dateipfad = Path(dateipfad) if dateipfad else (
            Path(__file__).parent / "data" / "pruefungsleistungen.json"
        )

    def laden(self):
        """Lädt Prüfungsleistungen als Mapping aus Modulcode und Domainobjekt."""
        if not self.dateipfad.exists():
            return {}

        with self.dateipfad.open("r", encoding="utf-8") as datei:
            daten = json.load(datei)

        pruefungsleistungen = {}
        for eintrag in daten:
            modul_code = eintrag["modul_code"]
            if modul_code in pruefungsleistungen:
                raise ValueError(f"Doppelter Modulcode in der Datendatei: {modul_code}")
            pruefungsleistungen[modul_code] = Pruefungsleistung(eintrag["note"])
        return pruefungsleistungen

    def speichern(self, pruefungsleistungen):
        """Speichert ein Mapping aus Modulcode und Prüfungsleistung."""
        self.dateipfad.parent.mkdir(parents=True, exist_ok=True)
        daten = [
            {"modul_code": modul_code, "note": pruefungsleistung.note}
            for modul_code, pruefungsleistung in sorted(pruefungsleistungen.items())
        ]
        with self.dateipfad.open("w", encoding="utf-8") as datei:
            json.dump(daten, datei, ensure_ascii=False, indent=2)
