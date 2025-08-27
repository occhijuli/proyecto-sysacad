import unittest
from datetime import date
from app.models.alumno import Alumno
from app.models.tipo_documento import TipoDocumento
from app.resources.pdf.alumno_pdf_exporter import AlumnoPDFExporter

class TestAlumnoPDFExporter(unittest.TestCase):
    def setUp(self):
        tipo_doc = TipoDocumento(nombre="DNI")
        self.alumno = Alumno(
            apellido="Pérez",
            nombre="Juan",
            nroDocumento="12345678",
            tipoDocumento=tipo_doc,
            fechaNacimiento="1995-06-15",
            sexo="M",
            nroLegajo=1001,
            fechaIngreso=date(2020, 3, 1)
        )
        self.exporter = AlumnoPDFExporter()

    def test_export_returns_bytes(self):
        pdf_bytes = self.exporter.export(self.alumno)
        self.assertIsInstance(pdf_bytes, bytes)
        self.assertGreater(len(pdf_bytes), 0)

    def test_pdf_contains_nombre(self):
        pdf_bytes = self.exporter.export(self.alumno)
        contenido = pdf_bytes.decode('latin-1', errors='ignore')
        self.assertIn("Juan", contenido)
        self.assertIn("Pérez", contenido)
        self.assertIn("Ficha del Alumno", contenido)

if __name__ == '__main__':
    unittest.main()
