from flask import Blueprint, render_template, session, redirect, url_for
from .database import get_connection

bp = Blueprint("routes", __name__)

# ----------------------------
# Página principal (productos)
# ----------------------------
@bp.route("/")
def index():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    conn.close()
    return render_template("index.html", productos=productos)

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

# ----------------------------
# Ver carrito
# ----------------------------
@bp.route("/cart")
def cart():
    cart_items = []
    total = 0

    if "cart" in session and session["cart"]:
        conn = get_connection()
        cursor = conn.cursor()

        for producto_id in session["cart"]:
            cursor.execute("SELECT * FROM productos WHERE id = ?", (producto_id,))
            producto = cursor.fetchone()
            if producto:
                # Calculamos subtotal y cantidad
                cantidad = session["cart"].count(producto[0])
                subtotal = producto[3] * cantidad  # Asumiendo columna precio es la 4ta
                total += subtotal
                cart_items.append({
                    "id": producto[0],
                    "nombre": producto[1],
                    "descripcion": producto[2],
                    "precio": producto[3],
                    "cantidad": cantidad,
                    "subtotal": subtotal
                })
        conn.close()

    return render_template("cart.html", carrito=cart_items, total=total)

# ----------------------------
# Eliminar un producto del carrito
# ----------------------------
@bp.route("/remove_from_cart/<int:producto_id>")
def remove_from_cart(producto_id):
    if "cart" in session:
        try:
            session["cart"].remove(producto_id)  # elimina solo una unidad
            session.modified = True
        except ValueError:
            pass
    return redirect(url_for("routes.cart"))

# ----------------------------
# Vaciar carrito completo
# ----------------------------
@bp.route("/clear_cart")
def clear_cart():
    session.pop("cart", None)
    return redirect(url_for("routes.cart"))
