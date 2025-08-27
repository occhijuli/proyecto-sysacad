from flask import Blueprint, Response, jsonify
from app.models.alumno import Alumno
from app.resources.alumno_json_exporter import AlumnoJSONExporter
from app.resources.pdf.alumno_pdf_exporter import AlumnoPDFExporter
import json

alumno_bp = Blueprint('alumno_bp', __name__)

@alumno_bp.route('/alumno/<int:legajo>/json', methods=['GET'])
def ficha_json(legajo):
    alumno = Alumno(legajo, "Pérez", "Juan", "Ingeniería")
    exporter = AlumnoJSONExporter()
    return jsonify(json.loads(exporter.export(alumno)))

@alumno_bp.route('/alumno/<int:legajo>/pdf', methods=['GET'])
def ficha_pdf(legajo):
    alumno = Alumno(legajo, "Pérez", "Juan", "Ingeniería")
    exporter = AlumnoPDFExporter()
    pdf_bytes = exporter.export(alumno)
    return Response(pdf_bytes, mimetype='application/pdf',
                    headers={"Content-Disposition": f"inline; filename=ficha_{legajo}.pdf"})
