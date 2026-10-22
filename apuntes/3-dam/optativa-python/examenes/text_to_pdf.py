import json
import random
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from reportlab.lib.colors import black
from datetime import datetime

# CONFIGURACIÓN
ARCHIVOS_JSON = ["tema_1.json", "tema_2.json", "tema_3.json"]
PREGUNTAS_POR_TEMA = 20
GENERAR_SOLUCIONES = True  # Cambia a False si no quieres el PDF de soluciones

def cargar_preguntas(archivo):
    with open(archivo, "r", encoding="utf-8") as f:
        return json.load(f)

def seleccionar_preguntas(preguntas, cantidad):
    return random.sample(preguntas, cantidad)

def dividir_pregunta_y_codigo(texto):
    """
    Divide la pregunta en parte interrogativa y parte de código (si hay).
    """
    if '?' in texto:
        idx = texto.index('?') + 1
        pregunta = texto[:idx].strip()
        codigo = texto[idx:].strip()
        return pregunta, codigo
    return texto.strip(), ""

def dibujar_codigo(c, x, y, codigo, ancho_max):
    """
    Dibuja líneas de código en fuente monoespaciada, sin fondo.
    """
    lineas = codigo.split("\n")
    alto_linea = 0.4 * cm
    c.setFont("Courier", 9)
    for linea in lineas:
        c.drawString(x, y, linea)
        y -= alto_linea
    return y

def crear_examen_pdf(preguntas, nombre_archivo, incluir_respuestas=False):
    c = canvas.Canvas(nombre_archivo, pagesize=A4)
    ancho, alto = A4
    y = alto - 2 * cm
    c.setFont("Helvetica-Bold", 14)
    c.drawString(2 * cm, y, "EXAMEN PYTHON - PROGRAMACIÓN")
    y -= 0.8 * cm
    c.setFont("Helvetica", 10)
    c.drawString(2 * cm, y, f"Fecha: {datetime.now().strftime('%d/%m/%Y')} - Total preguntas: {len(preguntas)}")
    y -= 1.5 * cm

    for idx, p in enumerate(preguntas, 1):
        if y < 6 * cm:
            c.showPage()
            y = alto - 2 * cm
            c.setFont("Helvetica", 11)

        pregunta_texto, codigo_extra = dividir_pregunta_y_codigo(p["Pregunta"])

        c.setFont("Helvetica", 11)
        c.drawString(2 * cm, y, f"{idx}. {pregunta_texto}")
        y -= 0.6 * cm

        if codigo_extra:
            y = dibujar_codigo(c, 2.6 * cm, y, codigo_extra, ancho_max=15 * cm)
            y -= 0.3 * cm

        c.setFont("Helvetica", 11)
        c.drawString(2.5 * cm, y, f"A) {p['A']}")
        y -= 0.5 * cm
        c.drawString(2.5 * cm, y, f"B) {p['B']}")
        y -= 0.5 * cm
        c.drawString(2.5 * cm, y, f"C) {p['C']}")
        y -= 0.5 * cm
        c.drawString(2.5 * cm, y, f"D) {p['D']}")
        y -= 0.6 * cm

        if incluir_respuestas:
            c.setFont("Helvetica-Oblique", 10)
            c.drawString(3 * cm, y, f"✔ Respuesta Correcta: {p['Respuesta Correcta']}")
            y -= 0.6 * cm

    c.save()

def main():
    todas_preguntas = []

    for archivo in ARCHIVOS_JSON:
        preguntas = cargar_preguntas(archivo)
        seleccionadas = seleccionar_preguntas(preguntas, PREGUNTAS_POR_TEMA)
        todas_preguntas.extend(seleccionadas)

    random.shuffle(todas_preguntas)

    crear_examen_pdf(todas_preguntas, "examen_python.pdf", incluir_respuestas=False)

    if GENERAR_SOLUCIONES:
        crear_examen_pdf(todas_preguntas, "examen_python_soluciones.pdf", incluir_respuestas=True)

    print("✅ Exámenes generados correctamente.")

if __name__ == "__main__":
    main()
