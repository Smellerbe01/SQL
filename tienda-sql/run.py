from app import create_app
from livereload import Server

app = create_app()

if __name__ == "__main__":
    server = Server(app.wsgi_app)

    # Vigilar cambios en templates y static
    server.watch("app/templates/")
    server.watch("app/static/")

    # Iniciar servidor con recarga automática
    server.serve(port=5000, debug=True)
