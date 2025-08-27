import json

class AlumnoJSONExporter:
    def export(self, alumno):
        return json.dumps(alumno.to_dict(), indent=4)
