"""
check_db.py

Script para verificar el contenido de la base de datos SQLite
dentro de la carpeta 'instance/'. Muestra el número de filas
de cada tabla principal.

Cómo usar:
1. Asegúrate de haber ejecutado init_db.py primero.
2. Ejecuta:
   python scripts/check_db.py
"""

import sqlite3
import os

# Carpeta donde está este script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Ruta de la base de datos dentro de instance/
DB_PATH = os.path.join(BASE_DIR, "..", "instance", "tienda.db")

# Verificar si la DB existe
if not os.path.exists(DB_PATH):
    print(f"No se encontró la base de datos en {DB_PATH}. Ejecuta init_db.py primero.")
    exit()

# Conectar a la base de datos
conn = sqlite3.connect(DB_PATH)
conn.row_factory = sqlite3.Row
