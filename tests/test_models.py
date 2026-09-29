"""Tests für das Domainmodell."""

import unittest

from models import Modul, ModulBelegung, Modulstatus, Pruefungsleistung


class PruefungsleistungTests(unittest.TestCase):
    def test_zehntelnote_bis_vier_ist_zulaessig_und_bestanden(self):
        pruefungsleistung = Pruefungsleistung("3,6")
        self.assertEqual(3.6, pruefungsleistung.note)
        self.assertTrue(pruefungsleistung.bestanden)

    def test_fuenf_ist_zulaessig_aber_nicht_bestanden(self):
        pruefungsleistung = Pruefungsleistung(5.0)
        self.assertFalse(pruefungsleistung.bestanden)

    def test_nicht_vorgesehene_noten_werden_abgewiesen(self):
        for note in (0.9, 4.1, 4.4, 5.5, 6.0):
            with self.subTest(note=note), self.assertRaises(ValueError):
                Pruefungsleistung(note)

    def test_note_kann_nicht_direkt_geaendert_werden(self):
        pruefungsleistung = Pruefungsleistung(1.7)
        with self.assertRaises(AttributeError):
            pruefungsleistung.note = 5.0
        self.assertEqual(1.7, pruefungsleistung.note)


class ModulBelegungTests(unittest.TestCase):
    def setUp(self):
        self.belegung = ModulBelegung(Modul("TEST", "Testmodul", 5))

    def test_status_wird_aus_pruefungsleistung_abgeleitet(self):
        self.assertEqual(Modulstatus.OFFEN, self.belegung.status)
        self.belegung.pruefungsleistung_eintragen(4.0)
        self.assertEqual(Modulstatus.ABGESCHLOSSEN, self.belegung.status)
        self.belegung.pruefungsleistung_eintragen(5.0)
        self.assertEqual(Modulstatus.NICHT_BESTANDEN, self.belegung.status)

    def test_pruefungsleistung_kann_nicht_direkt_ersetzt_werden(self):
        with self.assertRaises(AttributeError):
            self.belegung.pruefungsleistung = Pruefungsleistung(1.0)


if __name__ == "__main__":
    unittest.main()
