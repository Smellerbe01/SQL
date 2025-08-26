from app import create_app
from livereload import Server  # Solo si quieres recarga automática con Flask

app = create_app()

if __name__ == "__main__":
    # Usando livereload para ver cambios en templates y static
    server = Server(app.wsgi_app)
    server.watch("app/templates/")
    server.watch("app/static/")
    server.serve(port=5000, debug=True)
