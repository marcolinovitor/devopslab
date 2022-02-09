from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Hello World from DevOps & Cloud Lab! - Vitor Marcolino"

if __name__ == '__main__':
    port = os.getenv('PORT')
    app.run('0.0.0.0', port = port)