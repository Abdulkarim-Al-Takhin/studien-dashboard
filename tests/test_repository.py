"""Tests für die JSON-Persistenz."""

import tempfile
import unittest
from pathlib import Path

from models import Pruefungsleistung
from repository import PruefungsleistungRepository


class PruefungsleistungRepositoryTests(unittest.TestCase):
    def test_speichern_und_laden(self):
        with tempfile.TemporaryDirectory() as verzeichnis:
            repository = PruefungsleistungRepository(Path(verzeichnis) / "noten.json")
            repository.speichern({"MODUL-1": Pruefungsleistung(2.4)})

            geladene_daten = repository.laden()

            self.assertEqual(2.4, geladene_daten["MODUL-1"].note)

    def test_fehlende_datei_liefert_leeres_mapping(self):
        with tempfile.TemporaryDirectory() as verzeichnis:
            repository = PruefungsleistungRepository(Path(verzeichnis) / "fehlt.json")
            self.assertEqual({}, repository.laden())


if __name__ == "__main__":
    unittest.main()
