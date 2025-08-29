from flask import Blueprint, render_template, redirect, url_for, session
from .database import get_connection

# Definir el Blueprint
routes = Blueprint("routes", __name__)

# Página principal - lista los productos
@routes.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return render_template("index.html", productos=productos)

# Página del carrito
@routes.route("/cart")
def cart():
    # Recuperar IDs del carrito en sesión
    cart_items = session.get("cart", [])

    if not cart_items:
        return render_template("cart.html", cart=[])

    # Traer productos de la BD que estén en el carrito
    conn = get_connection()
    cursor = conn.cursor()
    placeholders = ",".join("?" * len(cart_items))  # genera ?,?,? según los IDs
    cursor.execute(f"SELECT * FROM productos WHERE producto_id IN ({placeholders})", cart_items)
    productos = cursor.fetchall()
    conn.close()

    return render_template("cart.html", cart=productos)

# Agregar producto al carrito
@routes.route("/add_to_cart/<int:producto_id>")
def add_to_cart(producto_id):
    cart = session.get("cart", [])
    cart.append(producto_id)
    session["cart"] = cart
    session.modified = True  # 🔥 necesario para que Flask guarde cambios
    return redirect(url_for("routes.cart"))

# Vaciar carrito
@routes.route("/clear_cart")
def clear_cart():
    session.pop("cart", None)  # elimina la variable de sesión
    return redirect(url_for("routes.cart"))
