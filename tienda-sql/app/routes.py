from flask import Blueprint, render_template, redirect, url_for, session, flash
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

# Agregar producto al carrito (sin abrir carrito)
@routes.route("/add_to_cart/<int:producto_id>")
def add_to_cart(producto_id):
    conn = get_connection()
    cursor = conn.cursor()

    # Verificar stock actual
    cursor.execute("SELECT stock FROM productos WHERE producto_id = ?", (producto_id,))
    producto = cursor.fetchone()
    if producto is None:
        conn.close()
        return redirect(url_for("routes.index"))

    stock_actual = producto["stock"]
    if stock_actual <= 0:
        conn.close()
        return redirect(url_for("routes.index"))

    # Reducir stock en 1
    cursor.execute(
        "UPDATE productos SET stock = stock - 1 WHERE producto_id = ?",
        (producto_id,)
    )
    conn.commit()
    conn.close()

    # Agregar al carrito en sesión
    cart = session.get("cart", [])
    cart.append(producto_id)
    session["cart"] = cart
    session.modified = True

    return redirect(url_for("routes.index"))



# Vaciar carrito
@routes.route("/clear_cart")
def clear_cart():
    cart = session.get("cart", [])

    if cart:
        conn = get_connection()
        cursor = conn.cursor()

        # Contar cuántas veces aparece cada producto en el carrito
        from collections import Counter
        conteo = Counter(cart)

        # Devolver stock a la base de datos
        for producto_id, cantidad in conteo.items():
            cursor.execute(
                "UPDATE productos SET stock = stock + ? WHERE producto_id = ?",
                (cantidad, producto_id)
            )
        conn.commit()
        conn.close()

    # Vaciar carrito de sesión
    session.pop("cart", None)
    return redirect(url_for("routes.cart"))


@routes.route("/remove_from_cart/<int:producto_id>")
def remove_from_cart(producto_id):
    cart = session.get("cart", [])

    if producto_id in cart:
        # Eliminar solo una unidad del carrito
        cart.remove(producto_id)
        session["cart"] = cart
        session.modified = True

        # Devolver stock a la base de datos
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "UPDATE productos SET stock = stock + 1 WHERE producto_id = ?",
            (producto_id,)
        )
        conn.commit()
        conn.close()

    return redirect(url_for("routes.cart"))
