from flask import Blueprint, render_template
from .database import get_connection

bp = Blueprint("routes", __name__)

@bp.route("/")
def index():
    conn = get_connection() # Obtener conexión a la base de datos
    cursor = conn.cursor()# Crear cursor para ejecutar consultas
    cursor.execute("SELECT * FROM productos")# Ejecutar consulta
    productos = cursor.fetchall()# Obtener todos los productos
    conn.close() # Cerrar conexión
    return render_template("index.html", productos=productos) # Renderizar plantilla con productos
