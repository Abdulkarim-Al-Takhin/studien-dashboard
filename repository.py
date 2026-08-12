import json
from pathlib import Path
from models import Pruefungsleistung



class PruefungsleistungRepository:
    """Lädt Prüfungsleistungen aus einer JSON-Datei."""

    def __init__(self):
        self.dateipfad = (
            Path(__file__).parent
            / "data"
            / "pruefungsleistungen.json"
        )

    def laden(self, studiengang):
        """Lädt die Prüfungsleistungen und ordnet sie den Modulen zu."""
        with open(self.dateipfad, "r", encoding="utf-8") as datei:
            daten = json.load(datei)

        pruefungsleistungen = []

        for eintrag in daten:
            modul = studiengang.finde_modul(
                eintrag["modul_id"]
            )

            if modul is None:
                raise ValueError(
                    "Das Modul mit der ID "
                    f"{eintrag['modul_id']} wurde nicht gefunden."
                )

            modul.aktualisiere_status(eintrag["note"])

            pruefungsleistung = Pruefungsleistung(
                note=eintrag["note"],
                modul=modul,
            )

            pruefungsleistungen.append(pruefungsleistung)

        return pruefungsleistungen

    def speichern(self, pruefungsleistungen):
        """Speichert alle prüfungsleistungen in der JSON-Datei"""
        daten = []

        for pruefung in pruefungsleistungen:
            eintrag = {
                "modul_id": pruefung.modul.modul_id,
                "note": pruefung.note,
            }

            daten.append(eintrag)

        with open(self.dateipfad, "w", encoding="utf-8") as datei:
            json.dump(
                daten,
                datei,
                ensure_ascii=False,
                indent=2,
            )