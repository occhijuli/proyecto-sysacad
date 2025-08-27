from fpdf import FPDF

class AlumnoPDFExporter:
    def export(self, alumno):
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Título
        pdf.cell(200, 10, txt="Ficha del Alumno", ln=True, align='C')
        pdf.ln(10)

        # Datos del alumno
        datos = alumno.to_dict()
        for key, value in datos.items():
            texto = f"{key.replace('_', ' ').capitalize()}: {value}"
            pdf.cell(200, 10, txt=texto, ln=True)

        return pdf.output(dest='S').encode('latin-1')  # Retorna como bytes
