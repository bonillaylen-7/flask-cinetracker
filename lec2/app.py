from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return "Bienvenido a mi API"

@app.route("/info", methods=["GET"])
def info():
    return {
        "nombre": "CineTracker API",
        "version": "1.0",
        "descripcion": "API para registrar y gestionar películas y series"
    }

@app.route("/mensaje", methods=["POST"])
def mensaje():
    data = request.json
    texto = data.get("mensaje", "Sin mensaje")
    return {"respuesta": f"Mensaje recibido: {texto}"}

if __name__ == "__main__":
    app.run(debug=True)
