from flask import Blueprint, render_template,session,redirect, url_for
from .database import get_connection

bp = Blueprint("routes", __name__)

# ----------------------------
# Página principal (productos)
# ----------------------------
@bp.route("/")
def index():
    conn = get_connection() # Obtener conexión a la base de datos
    cursor = conn.cursor()# Crear cursor para ejecutar consultas
    cursor.execute("SELECT * FROM productos")# Ejecutar consulta
    productos = cursor.fetchall()# Obtener todos los productos
    conn.close() # Cerrar conexión
    return render_template("index.html", productos=productos) # Renderizar plantilla con productos



# ----------------------------
# Agregar al carrito
# ----------------------------
@bp.route("/add_to_cart/<int:producto_id>")
def add_to_cart(producto_id):
    if "cart" not in session:
        session["cart"] = []
    session["cart"].append(producto_id)
    session.modified = True
    return redirect(url_for("routes.cart"))

