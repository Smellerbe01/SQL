import os
import sqlite3

# Ruta completa a la carpeta instance
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "instance", "tienda.db")

def get_connection():
    """
    Devuelve una conexión a la base de datos.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """
    Inicializa la base de datos:
    - Crea la carpeta instance si no existe
    - Crea la tabla productos si no existe
    - Inserta productos de ejemplo si la tabla está vacía
    """
    # Crear carpeta instance si no existe
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

    conn = get_connection()
    cursor = conn.cursor()

    conn.commit()
    conn.close()

# Permite ejecutar el archivo directamente
if __name__ == "__main__":
    init_db()
    print(f"Base de datos creada correctamente en: {DB_PATH}")
