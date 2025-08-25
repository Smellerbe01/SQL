import sqlite3
import os

# Carpeta donde está este script
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Rutas a los archivos SQL
SCHEMA_PATH = os.path.join(BASE_DIR, "schema.sql")
SEED_PATH = os.path.join(BASE_DIR, "seed.sql")

# Ruta de la DB dentro de instance/
DB_PATH = os.path.join(BASE_DIR, "..", "instance", "tienda.db")
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Borrar base de datos existente (para desarrollo)
if os.path.exists(DB_PATH):
    os.remove(DB_PATH)
    print(f"🗑  Base de datos existente eliminada: {DB_PATH}")

# Conectar y ejecutar scripts
conn = sqlite3.connect(DB_PATH)

with open(SCHEMA_PATH, "r", encoding="utf-8") as f:
    conn.executescript(f.read())

with open(SEED_PATH, "r", encoding="utf-8") as f:
    conn.executescript(f.read())

conn.commit()
conn.close()

print(f"Base de datos creada y poblada en {DB_PATH}")
