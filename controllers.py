"""Web-Controller des Studien-Dashboards."""

from flask import redirect, render_template, request, url_for


class DashboardController:
    def __init__(self, service):
        self.service = service

    def registriere_routen(self, app):
        """Ordnet HTTP-Routen den Controller-Methoden zu."""
        app.add_url_rule("/", "dashboard", self.dashboard, methods=["GET"])
        app.add_url_rule(
            "/pruefungsleistung/eintragen",
            "pruefungsleistung_eintragen",
            self.pruefungsleistung_eintragen,
            methods=["POST"],
        )

    def dashboard(self):
        return render_template("dashboard.html", **self.service.dashboard_daten())

    def pruefungsleistung_eintragen(self):
        modul_code = request.form.get("modul_code", "")
        note = request.form.get("note", "")
        try:
            self.service.pruefungsleistung_eintragen(modul_code, note)
        except (ValueError, KeyError) as fehler:
            daten = self.service.dashboard_daten()
            daten["fehlermeldung"] = str(fehler)
            return render_template("dashboard.html", **daten), 400
        return redirect(url_for("dashboard"))
