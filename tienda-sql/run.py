from app import create_app
from livereload import Server

app = create_app()
app.config["DEBUG"] = True  # Activa modo debug de Flask

if __name__ == "__main__":
    server = Server(app.wsgi_app)

    # Vigilar cambios en templates y archivos estáticos
    server.watch("app/templates/")
    server.watch("app/static/")

    # Inicia el servidor en el puerto 5000
    server.serve(port=5000, debug=True)
