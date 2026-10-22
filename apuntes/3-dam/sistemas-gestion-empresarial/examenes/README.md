# Sistema de Gestión de Exámenes - SGE DAM

## Descripción
Aplicación para la gestión y realización de exámenes del módulo de Sistemas de Gestión Empresarial (SGE) para el ciclo formativo de DAM. La aplicación permite generar exámenes aleatorios a partir de un banco de preguntas organizado por temas.

## Características Principales
- Generación aleatoria de exámenes
- Banco de preguntas en formato JSON
- Sistema de evaluación automática
- Retroalimentación inmediata de respuestas
- Estadísticas finales del examen

## Estructura del Proyecto
```
/EXAMENES
├── tema_1.json         # Preguntas del tema 1
├── tema_2.json         # Preguntas del tema 2
├── tema_3.json         # Preguntas del tema 3
├── tema_4.json         # Preguntas del tema 4
├── tema_5.json         # Preguntas del tema 5
├── ExamenSGE.py       # Script principal
└── README.md          # Documentación
```

## Funcionamiento
1. La aplicación carga preguntas desde archivos JSON
2. Selecciona 10 preguntas aleatorias de cada tema
3. Mezcla las preguntas para crear un examen de 50 preguntas
4. Permite al usuario responder cada pregunta (A/B/C/D)
5. Muestra retroalimentación inmediata tras cada respuesta
6. Al finalizar, presenta estadísticas del examen

## Formato de Preguntas (JSON)
```json
{
    "Pregunta": "Texto de la pregunta",
    "A": "Opción A",
    "B": "Opción B",
    "C": "Opción C",
    "D": "Opción D",
    "Respuesta Correcta": "X"  // Donde X es A, B, C o D
}
```

## Requisitos Técnicos
- Python 3.x
- Bibliotecas estándar de Python (json, random)
- Archivos JSON con el banco de preguntas
- IDE recomendado: Visual Studio Code

## Instrucciones de Uso
1. Clonar el repositorio
2. Ejecutar el script principal:
```bash
python ExamenSGE.py
```
3. Seguir las instrucciones en pantalla
4. Responder cada pregunta con A, B, C, D o Enter para omitir

## Evaluación
- Respuestas correctas: +1 punto
- Respuestas incorrectas: no restan
- Preguntas sin responder: 0 puntos
- Se muestra resumen final con aciertos, fallos y omisiones

## Autor
DMIAPER

## Licencia
Uso Educativo
