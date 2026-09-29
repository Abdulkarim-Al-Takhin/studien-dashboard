"""Programmeinstieg und Aufbau der Flask-Anwendung."""

from flask import Flask

from controllers import DashboardController
from repository import PruefungsleistungRepository
from services import DashboardService
from study_plan import erstelle_student_mit_studienplan


def create_app(student=None, repository=None):
    """Erzeugt die Anwendung und verbindet ihre Schichten."""
    app = Flask(__name__)
    student = student or erstelle_student_mit_studienplan()
    repository = repository or PruefungsleistungRepository()
    service = DashboardService(student, repository)
    service.lade_pruefungsleistungen()
    DashboardController(service).registriere_routen(app)
    return app


app = create_app()


if __name__ == "__main__":
    app.run(debug=True)
