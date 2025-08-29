import os
import sqlite3

# Ruta de la base de datos dentro de /instance
DB_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "instance", "tienda.db")

def get_connection():
    """
    Devuelve una conexión a la base de datos SQLite.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Permite acceder a columnas como diccionario
    return conn
