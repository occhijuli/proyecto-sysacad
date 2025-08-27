import unittest
from datetime import date
from app.models.alumno import Alumno
from app.models.tipo_documento import TipoDocumento
from app.resources.pdf.alumno_pdf_exporter import AlumnoPDFExporter

class TestAlumnoPDFExporter(unittest.TestCase):
    def setUp(self):
        # ✅ SRP – Principio de Responsabilidad Única
        # La clase AlumnoPDFExporter tiene una única responsabilidad: exportar PDFs.
        # Esto permite testearla de forma aislada y clara.
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
        # ✅ TDD: Este test fue escrito antes de implementar el método export().
        # ✅ SRP: Validamos que la clase cumple su única responsabilidad.
        pdf_bytes = self.exporter.export(self.alumno)
        self.assertIsInstance(pdf_bytes, bytes)
        self.assertGreater(len(pdf_bytes), 0)

    def test_pdf_contains_nombre(self):
        # ✅ TDD: Validamos que el PDF generado contiene el nombre del alumno.
        # ✅ OCP – Principio de Abierto/Cerrado
        # Podemos agregar nuevos tests sin modificar la clase exportadora.
        pdf_bytes = self.exporter.export(self.alumno)
        contenido = pdf_bytes.decode('latin-1', errors='ignore')
        self.assertIn("Juan", contenido)
        self.assertIn("Pérez", contenido)
        self.assertIn("Ficha del Alumno", contenido)

if __name__ == '__main__':
    unittest.main()
