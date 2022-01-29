from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World from DevOps & Cloud Lab! - Vitor Marcolino"

if __name__ == '__main__':
    app.run()