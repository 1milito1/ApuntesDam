# Generador de Exámenes Python

Este proyecto implementa un sistema de generación de exámenes tipo test de Python, con dos modalidades: generación de PDFs y modo interactivo por consola.

## Descripción

El proyecto consta de dos scripts principales:

1. text_to_pdf.py: Genera exámenes en formato PDF
2. examen_gen.py: Permite realizar el examen de forma interactiva

## Requisitos

### Librerías necesarias

```bash
pip install reportlab
```

## Características

### Generador PDF (text_to_pdf.py)
- Genera dos versiones del examen:
  - Versión sin respuestas (examen_python.pdf)
  - Versión con respuestas (examen_python_soluciones.pdf)
- Formato profesional con paginación automática
- Soporte para código fuente con formato
- Fecha automática en cada examen

### Generador Interactivo (examen_gen.py)
- Interfaz por consola
- Retroalimentación inmediata
- Estadísticas finales
- Sistema de validación de respuestas

## Estructura del Proyecto

```
├── text_to_pdf.py
├── examen_gen.py
├── tema_1.json
├── tema_2.json
└── tema_3.json
```

## Configuración

El proyecto utiliza archivos JSON para almacenar las preguntas. Cada archivo debe seguir esta estructura:

```json
[
    {
        "Pregunta": "¿Texto de la pregunta?",
        "A": "Opción A",
        "B": "Opción B",
        "C": "Opción C",
        "D": "Opción D",
        "Respuesta Correcta": "A"
    }
]
```

### Variables Configurables

En text_to_pdf.py:
- `PREGUNTAS_POR_TEMA`: Número de preguntas por tema (default: 20)
- `GENERAR_SOLUCIONES`: Genera PDF con respuestas (default: True)

## Uso

### Generar exámenes en PDF
```bash
python text_to_pdf.py
```

### Ejecutar examen interactivo
```bash
python examen_gen.py
```

## Requisitos del Sistema
- Python 3.x
- ReportLab (para generación de PDFs)
- Sistema operativo: Windows, Linux o macOS

## Notas Adicionales
- Los archivos JSON deben estar en el mismo directorio que los scripts
- Las preguntas se seleccionan aleatoriamente de cada tema
- El formato de las respuestas debe ser A, B, C o D

## Autor
DMIAPER

## Licencia
Uso educativo