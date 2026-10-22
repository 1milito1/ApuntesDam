import json
import random

def cargar_preguntas(rutas_archivos):
    preguntas_totales = []
    for ruta in rutas_archivos:
        with open(ruta, "r", encoding="utf-8") as f:
            preguntas = json.load(f)
            preguntas_totales.extend(preguntas)
    return preguntas_totales

def seleccionar_preguntas(preguntas, n):
    if len(preguntas) < n:
        raise ValueError(f"No hay suficientes preguntas: se requieren {n}, pero hay {len(preguntas)}")
    return random.sample(preguntas, n)

def main():
    # Archivos JSON con preguntas de cada tema
    archivos_json = ["tema_1.json", "tema_2.json", "tema_3.json"]

    # Cargar preguntas de cada archivo
    preguntas_tema1 = cargar_preguntas([archivos_json[0]])
    preguntas_tema2 = cargar_preguntas([archivos_json[1]])
    preguntas_tema3 = cargar_preguntas([archivos_json[2]])

    # Seleccionar 20 preguntas de cada tema
    seleccion_tema1 = seleccionar_preguntas(preguntas_tema1, 20)
    seleccion_tema2 = seleccionar_preguntas(preguntas_tema2, 20)
    seleccion_tema3 = seleccionar_preguntas(preguntas_tema3, 20)

    # Unir y mezclar
    examen = seleccion_tema1 + seleccion_tema2 + seleccion_tema3
    random.shuffle(examen)

    respuestas_usuario = []
    print("Responde cada pregunta con A, B, C, D o deja vacío y pulsa Enter para no responder.\n")

    for idx, pregunta in enumerate(examen, 1):
        print(f"Pregunta {idx}: {pregunta['Pregunta']}")
        print(f"A) {pregunta['A']}")
        print(f"B) {pregunta['B']}")
        print(f"C) {pregunta['C']}")
        print(f"D) {pregunta['D']}")

        respuesta = input("Tu respuesta (A/B/C/D) o Enter para no responder: ").strip().upper()
        while respuesta not in ["A", "B", "C", "D", ""]:
            print("Respuesta inválida. Por favor ingresa A, B, C, D o deja vacío.")
            respuesta = input("Tu respuesta (A/B/C/D) o Enter para no responder: ").strip().upper()

        respuestas_usuario.append({
            "pregunta": pregunta["Pregunta"],
            "respuesta_correcta": pregunta["Respuesta Correcta"].upper(),
            "respuesta_usuario": respuesta if respuesta else None
        })

        # Mostrar si la respuesta fue correcta o no, y cuál era la correcta
        if respuesta == "":
            print(f"No respondiste. La respuesta correcta era: {pregunta['Respuesta Correcta'].upper()})\n")
        elif respuesta == pregunta["Respuesta Correcta"].upper():
            print("¡Correcto!\n")
        else:
            print(f"Incorrecto. La respuesta correcta es: {pregunta['Respuesta Correcta'].upper()}\n")

    # Evaluar resultados
    aciertos = sum(1 for r in respuestas_usuario if r["respuesta_usuario"] == r["respuesta_correcta"])
    fallos = sum(1 for r in respuestas_usuario if r["respuesta_usuario"] is not None and r["respuesta_usuario"] != r["respuesta_correcta"])
    no_respondidas = sum(1 for r in respuestas_usuario if r["respuesta_usuario"] is None)

    print(f"Examen terminado.\nAciertos: {aciertos}\nFallos: {fallos}\nNo respondidas: {no_respondidas}\n")

    if no_respondidas > 0:
        print("Preguntas no respondidas:")
        for r in respuestas_usuario:
            if r["respuesta_usuario"] is None:
                print(f"- {r['pregunta']} (Respuesta correcta: {r['respuesta_correcta']})")

if __name__ == "__main__":
    main()
