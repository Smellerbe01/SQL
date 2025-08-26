# SQL
casos de practica de SQL
En este caso voy a crear una pagina web para una pequeña tienda 
en ella usare una base de datos sencilla 

1. creare la estructura de la tienda
### texto de prueba 
```bash
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
## Recordar actualizar el pip install
python.exe -m pip install --upgrade pip

# voy a usar un entorno virtual para instalar, ejecutar y desplegar los cambios 
1. mi carpeta general o principal se llama tienda-sql, por lo que ubicamos la terminal en la tienda
   con el comando cd tienda-sql

2. inicializo el entorno virtual con:
    python -m venv venv

3. activo los scripts del entorno virtual
    venv\Scripts\activate

4. Instalar Flask y Livereload
    pip install flask livereload

5. guardamos dependencias:
    pip freeze > requirements.txt

