"""Integrationstests für die Flask-Routen."""

import tempfile
import unittest
from pathlib import Path

from app import create_app
from repository import PruefungsleistungRepository
from study_plan import erstelle_student_mit_studienplan


class DashboardAppTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.repository = PruefungsleistungRepository(Path(self.temp.name) / "noten.json")
        app = create_app(erstelle_student_mit_studienplan(), self.repository)
        app.config.update(TESTING=True)
        self.client = app.test_client()

    def tearDown(self):
        self.temp.cleanup()

    def test_dashboard_ist_erreichbar(self):
        response = self.client.get("/")
        self.assertEqual(200, response.status_code)
        self.assertIn("Mein Studien-Dashboard", response.get_data(as_text=True))

    def test_zulaessige_note_wird_gespeichert(self):
        response = self.client.post(
            "/pruefungsleistung/eintragen",
            data={"modul_code": "DLBDSEAIS01-01_D", "note": "3,6"},
        )
        self.assertEqual(302, response.status_code)
        self.assertEqual(3.6, self.repository.laden()["DLBDSEAIS01-01_D"].note)

    def test_unzulaessige_note_wird_abgewiesen(self):
        response = self.client.post(
            "/pruefungsleistung/eintragen",
            data={"modul_code": "DLBDSEAIS01-01_D", "note": "4,4"},
        )
        self.assertEqual(400, response.status_code)
        self.assertEqual({}, self.repository.laden())


if __name__ == "__main__":
    unittest.main()
