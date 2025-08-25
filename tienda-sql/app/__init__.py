from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True

    # Importar rutas
    from . import routes
    app.register_blueprint(routes.bp)

    # Inicializar la base de datos
    from .database import init_db
    init_db()

    return app
