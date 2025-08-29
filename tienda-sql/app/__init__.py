from flask import Flask

def create_app():
    app = Flask(__name__)
    app.secret_key = "supersecretkey"  # Necesario para usar session

    # Importar y registrar el blueprint
    from .routes import routes
    app.register_blueprint(routes)

    return app
