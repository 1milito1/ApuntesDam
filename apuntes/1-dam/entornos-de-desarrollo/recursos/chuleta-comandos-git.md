# Guía Rápida de Git para DAM
*Aprende a dominar el control de versiones en tus proyectos.*

## 1. Configuración Inicial
```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu_correo@gmail.com"
```

## 2. Flujo Diario de Trabajo
```bash
git status               # Ver archivos modificados
git add .                # Añadir todos los cambios al stage
git commit -m "Mensaje"  # Confirmar cambios
git push origin main     # Subir al repositorio remoto
```

## 3. Trabajo con Ramas (Branches)
```bash
git checkout -b feature/login    # Crear y cambiar a nueva rama
git branch                       # Listar ramas locales
git checkout main                # Volver a main
git merge feature/login          # Fusionar rama en la actual
```