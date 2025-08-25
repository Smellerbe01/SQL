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

    # Crear tabla productos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            descripcion TEXT,
            precio REAL NOT NULL
        )
    ''')

    # Agregar productos de ejemplo si la tabla está vacía
    cursor.execute("SELECT COUNT(*) FROM productos")
    if cursor.fetchone()[0] == 0:
        productos = [
            ("Producto 1", "Descripción corta del producto 1", 10.99),
            ("Producto 2", "Descripción corta del producto 2", 15.50),
            ("Producto 3", "Descripción corta del producto 3", 7.25),
            ("Producto 4", "Descripción corta del producto 4", 12.00)
        ]
        cursor.executemany(
            "INSERT INTO productos (nombre, descripcion, precio) VALUES (?, ?, ?)",
            productos
        )

    conn.commit()
    conn.close()

# Permite ejecutar el archivo directamente
if __name__ == "__main__":
    init_db()
    print(f"Base de datos creada correctamente en: {DB_PATH}")
