# 📚 Repositorio y Web de Apuntes DAM (GitHub Pages Ready)

Sitio web moderno, rápido y responsive con **592 documentos oficiales clasificados y anonimizados** (temarios, exámenes anteriores con soluciones, prácticas, enunciados y chuletas) para el ciclo de **Desarrollo de Aplicaciones Multiplataforma (DAM)**.

Incluye una **aplicación de escritorio complementaria en Python (PyQt5)** para importar nuevos documentos con un clic, clasificarlos automáticamente en la estructura de carpetas adecuada y sincronizarlos con GitHub Pages.

---

## 🌟 Resumen del Catálogo Organizado

- **592 documentos educativos limpios** listos para consultar y descargar.
- **100% Anónimo y Privado**: Se han purgado todos los documentos que contenían datos personales o nombres de autor.
- **14 asignaturas cubiertas** repartidas en los 3 cursos académicos de tu FP:
  - **1º Curso**: Programación, Bases de Datos, Sistemas Informáticos, Entornos de Desarrollo, Lenguajes de Marcas.
  - **2º Curso**: Bases de Datos II (Avanzada/NoSQL), Lenguajes de Marcas II (XML/JSON), Prog. de Servicios y Procesos (PSP), Inglés Técnico, Itinerario de Empleabilidad (IPE / FOL).
  - **3º Curso / Especialización**: Desarrollo de Interfaces (JavaFX/Swing/JasperReports), Prog. Multimedia y Dispositivos Móviles (Android), Sistemas de Gestión Empresarial (SGE/Odoo), Optativa (Python).
- **Tamaño total optimizado**: **760 MB** (perfectamente ajustado por debajo del límite de 1 GB de GitHub Pages y sin ningún archivo individual que supere los límites de Git).

---

## 📂 Estructura del Proyecto

```text
dam-apuntes/
│
├── index.html                  # Página web principal (publicada en GitHub Pages)
├── iniciar_gestor.bat          # Doble clic para abrir el gestor gráfico en Windows
├── gestor_desktop.py           # App de escritorio para clasificar y publicar apuntes
├── css/
│   └── style.css               # Sistema de diseño moderno, temas claro/oscuro y responsive
├── js/
│   ├── app.js                  # Lógica del buscador, filtros, modal y paginación rápida
│   └── data.js                 # Datos precargados con los 592 documentos para ver offline
├── data/
│   └── apuntes.json            # Base de datos JSON con el catálogo de todos los apuntes
└── apuntes/                    # Estructura normalizada de documentos
    ├── 1-dam/                  # 1º Curso (Programación, BBDD, SI, ED, LMSG)
    ├── 2-dam/                  # 2º Curso (BBDD2, LMSG2, PSP, Inglés, IPE/FOL)
    └── 3-dam/                  # 3º Curso (Interfaces, Móviles, SGE, Python)
```

---

## 🚀 Cómo poner la web en GitHub Pages (Paso a Paso)

1. **Crea un nuevo repositorio en GitHub**:
   - Ve a [github.com/new](https://github.com/new).
   - Nómbralo por ejemplo `apuntes-dam`.
   - Déjalo como **Público** (para que GitHub Pages sea gratis).

2. **Sube este proyecto a tu repositorio**:
   Abre una terminal en esta carpeta y ejecuta:
   ```bash
   git init
   git add .
   git commit -m "Lanzamiento web de apuntes oficiales de DAM"
   git branch -M main
   git remote add origin https://github.com/TU-USUARIO/apuntes-dam.git
   git push -u origin main
   ```

3. **Activar GitHub Pages**:
   - En tu repositorio de GitHub, entra en **Settings** (Configuración) > **Pages**.
   - En **Build and deployment > Source**, selecciona: `Deploy from a branch`.
   - En **Branch**, selecciona `main` y la carpeta `/(root)`.
   - Haz clic en **Save** (Guardar).
   - En 1 minuto tu web estará disponible para compartir en:
     `https://TU-USUARIO.github.io/apuntes-dam/`

---

## 🖥️ Cómo usar la App de Escritorio para nuevos apuntes

1. Haz doble clic en **`iniciar_gestor.bat`**.
2. Selecciona cualquier archivo (PDF, Word, SQL, ZIP, Python...).
3. Elige curso, asignatura y categoría.
4. Pulsa **"✨ Importar, Clasificar en su Carpeta y Actualizar Web"**.
5. En la pestaña **"🚀 Publicar en GitHub Pages"**, pulsa un botón para subir los cambios a internet.
