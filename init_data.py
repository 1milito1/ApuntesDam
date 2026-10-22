import os
import json

BASE_DIR = r"C:\Users\milio\.gemini\antigravity-ide\scratch\dam-apuntes"

STRUCTURE = {
    "cursos": [
        {
            "id": "1-dam",
            "name": "1º DAM",
            "description": "Primer curso: Fundamentos de programación, sistemas, bases de datos y marcas",
            "asignaturas": [
                {
                    "id": "programacion",
                    "name": "Programación",
                    "code": "PROG",
                    "icon": "code",
                    "color": "#3b82f6",
                    "description": "Java, POO, estructuras de datos, modularidad y ficheros"
                },
                {
                    "id": "bases-de-datos",
                    "name": "Bases de Datos",
                    "code": "BBDD",
                    "icon": "database",
                    "color": "#10b981",
                    "description": "SQL, diseño relacional, normalización, MySQL y PostgreSQL"
                },
                {
                    "id": "sistemas-informaticos",
                    "name": "Sistemas Informáticos",
                    "code": "SI",
                    "icon": "server",
                    "color": "#8b5cf6",
                    "description": "Hardware, Linux, Windows Server, redes y virtualización"
                },
                {
                    "id": "entornos-de-desarrollo",
                    "name": "Entornos de Desarrollo",
                    "code": "ED",
                    "icon": "git-branch",
                    "color": "#f59e0b",
                    "description": "Git, GitHub, pruebas unitarias JUnit, refactorización y diagramas UML"
                },
                {
                    "id": "lenguajes-de-marcas",
                    "name": "Lenguajes de Marcas",
                    "code": "LND",
                    "icon": "file-code",
                    "color": "#ec4899",
                    "description": "HTML5, CSS3, XML, JSON, XPath, XQuery y XSLT"
                },
                {
                    "id": "fol-ipe",
                    "name": "FOL / IPE",
                    "code": "FOL",
                    "icon": "briefcase",
                    "color": "#64748b",
                    "description": "Formación y Orientación Laboral, contratos, nóminas, PRL y empleabilidad"
                }
            ]
        },
        {
            "id": "2-dam",
            "name": "2º DAM",
            "description": "Segundo curso: Especialización en interfaces, móvil, servicios y persistencia avanzada",
            "asignaturas": [
                {
                    "id": "acceso-a-datos",
                    "name": "Acceso a Datos",
                    "code": "AD",
                    "icon": "layers",
                    "color": "#06b6d4",
                    "description": "JDBC, Hibernate, JPA, Spring Data, bases de datos NoSQL y MongoDB"
                },
                {
                    "id": "desarrollo-de-interfaces",
                    "name": "Desarrollo de Interfaces",
                    "code": "DI",
                    "icon": "layout",
                    "color": "#a855f7",
                    "description": "JavaFX, Qt/Python, diseño UX/UI, componentes gráficos e informes Jasper"
                },
                {
                    "id": "programacion-multimedia",
                    "name": "Prog. Multimedia y Móviles",
                    "code": "PMDM",
                    "icon": "smartphone",
                    "color": "#14b8a6",
                    "description": "Android Studio, Kotlin, arquitectura MVVM, Jetpack Compose y APIs"
                },
                {
                    "id": "programacion-servicios-procesos",
                    "name": "Prog. Servicios y Procesos",
                    "code": "PSP",
                    "icon": "cpu",
                    "color": "#ef4444",
                    "description": "Concurrencia, hilos/threads, sockets TCP/UDP, criptografía y servicios web"
                },
                {
                    "id": "sistemas-gestion-empresarial",
                    "name": "Sistemas de Gestión Empresarial",
                    "code": "SGE",
                    "icon": "settings",
                    "color": "#f97316",
                    "description": "ERP, CRM, Odoo, módulos en Python y flujos de negocio"
                },
                {
                    "id": "empresa-iniciativa",
                    "name": "Empresa e Iniciativa Emprendedora",
                    "code": "EIE",
                    "icon": "trending-up",
                    "color": "#84cc16",
                    "description": "Plan de empresa, formas jurídicas, fiscalidad y marketing"
                }
            ]
        }
    ],
    "categorias": [
        {"id": "temarios", "name": "Temarios y Apuntes", "icon": "book-open", "badgeClass": "badge-temario"},
        {"id": "examenes", "name": "Exámenes Anteriores", "icon": "award", "badgeClass": "badge-examen"},
        {"id": "tareas", "name": "Tareas y Prácticas", "icon": "check-square", "badgeClass": "badge-tarea"},
        {"id": "recursos", "name": "Chuletas y Recursos de Ayuda", "icon": "zap", "badgeClass": "badge-recurso"}
    ]
}

# Create all folders
for curso in STRUCTURE["cursos"]:
    for asig in curso["asignaturas"]:
        for cat in STRUCTURE["categorias"]:
            folder = os.path.join(BASE_DIR, "apuntes", curso["id"], asig["id"], cat["id"])
            os.makedirs(folder, exist_ok=True)

# Also ensure data and assets folders
os.makedirs(os.path.join(BASE_DIR, "data"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "css"), exist_ok=True)
os.makedirs(os.path.join(BASE_DIR, "js"), exist_ok=True)

print("Folders created successfully.")
