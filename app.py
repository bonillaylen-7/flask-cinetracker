from flask import Flask, jsonify, request

app = Flask(__name__)

# Lista de usuarios almacenados en memoria
usuarios = []

@app.route("/info", methods=["GET"])
def info():
    return jsonify({
        "nombre": "CineTracker API",
        "version": "1.0",
        "descripcion": "API para registrar y gestionar películas y series",
        "rutas_disponibles": ["/info", "/crear_usuario", "/usuarios"]
    })

@app.route("/crear_usuario", methods=["POST"])
def crear_usuario():
    data = request.json
    if not data or "nombre" not in data or "correo" not in data:
        return jsonify({"error": "Datos incompletos, se requiere nombre y correo"}), 400
    nuevo_usuario = {
        "id": len(usuarios) + 1,
        "nombre": data["nombre"],
        "correo": data["correo"]
    }
    usuarios.append(nuevo_usuario)
    return jsonify({"mensaje": "Usuario creado exitosamente!", "usuario": nuevo_usuario}), 201

@app.route("/usuarios", methods=["GET"])
def obtener_usuarios():
    return jsonify({"usuarios": usuarios})

if __name__ == "__main__":
    app.run(debug=True)