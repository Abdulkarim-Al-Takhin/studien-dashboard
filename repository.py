"""Persistenzschicht für Prüfungsleistungen."""

import json
from pathlib import Path
from typing import Dict

class PruefungsleistungRepository:
    """Speichert Prüfungsleistungen getrennt von der Anwendungslogik als JSON."""

    def __init__(self, dateipfad=None):
        self.dateipfad = Path(dateipfad) if dateipfad else (
            Path(__file__).parent / "data" / "pruefungsleistungen.json"
        )

    def laden(self) -> Dict[str, float]:
        """
        Lädt Prüfungsleistungen als einfaches Mapping (Dict).
        Rückgabe: { 'MODUL_CODE': note_als_float }
        """
        if not self.dateipfad.exists():
            return {}

        with self.dateipfad.open("r", encoding="utf-8") as datei:
            daten = json.load(datei)

        # Wir wandeln die Liste aus der JSON in ein Dictionary um
        # Damit erfüllen wir die Anforderung des Tutors: laden() -> Dict
        return {eintrag["modul_code"]: float(eintrag["note"]) for eintrag in daten}

    def speichern(self, pruefungsleistungen_dict: Dict[str, float]):
        """
        Speichert ein Mapping aus Modulcode und Note.
        Erwartet: { 'MODUL_CODE': note_als_float }
        """
        self.dateipfad.parent.mkdir(parents=True, exist_ok=True)

        # Wir wandeln das Dict zurück in die Listen-Struktur für die JSON-Datei
        daten = [
            {"modul_code": code, "note": note}
            for code, note in sorted(pruefungsleistungen_dict.items())
        ]
        with self.dateipfad.open("w", encoding="utf-8") as datei:
            json.dump(daten, datei, ensure_ascii=False, indent=2)
