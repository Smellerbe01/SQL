# SQL
casos de practica de SQL
En este caso voy a crear una pagina web para una pequeña tienda 
en ella usare una base de datos sencilla 

1. creare la estructura de la tienda

    tienda-sql/
│
├── run.py                  # Punto de entrada (ejecuta la app con Livereload)
│
├── app/                    # Carpeta principal de la aplicación
│   ├── __init__.py         # Crea la app Flask y conecta con la DB
│   ├── routes.py           # Rutas y lógica de la tienda
│   │
│   ├── templates/          # Archivos HTML (Jinja2 templates)
│   │   └── index.html
│   │
│   ├── static/             # Archivos estáticos (CSS, imágenes, JS)
│   │   └── style.css
│   │
│   └── __pycache__/        # Archivos temporales (se generan solos)
│
├── instance/               # Carpeta para la DB y configs locales
│   └── tienda.db           # Base de datos SQLite
│
├── venv/                   # Entorno virtual de Python
│
└── requirements.txt        # Lista de dependencias (Flask, livereload, etc.)


## Comandos básicos de Git

```bash
git init             # Inicializa un repositorio Git
git status           # Muestra el estado de los archivos
git add .            # Agrega todos los archivos al área de staging
git commit -m "mensaje"  # Realiza un commit con mensaje
git log              # Muestra el historial de commits
git branch           # Lista las ramas
git checkout rama    # Cambia a la rama especificada
git merge rama       # Fusiona la rama especificada con la actual
git pull             # Descarga y fusiona cambios del repositorio remoto
git push             # Sube los cambios al repositorio remoto
```
## 