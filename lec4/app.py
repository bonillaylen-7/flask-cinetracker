from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {
        "title": "CineTracker",
        "message": "Tu gestor personal de películas y series"
    }
    return render_template('index.html', data=data)

@app.route('/peliculas')
def peliculas():
    peliculas = [
        {"id": 1, "titulo": "Inception", "genero": "Ciencia Ficción", "año": 2010, "estado": "Vista", "calificacion": "⭐⭐⭐⭐⭐"},
        {"id": 2, "titulo": "The Batman", "genero": "Acción", "año": 2022, "estado": "Pendiente", "calificacion": "Sin calificar"},
        {"id": 3, "titulo": "Interstellar", "genero": "Ciencia Ficción", "año": 2014, "estado": "Vista", "calificacion": "⭐⭐⭐⭐⭐"},
    ]
    return render_template('peliculas.html', peliculas=peliculas)

@app.route('/usuarios')
def usuarios():
    usuarios = [
        {"id": 1, "nombre": "Manuel Velez", "correo": "manuel890@gmail.com", "peliculas_vistas": 2},
        {"id": 2, "nombre": "Ana García", "correo": "ana@gmail.com", "peliculas_vistas": 5},
    ]
    return render_template('usuarios.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run(debug=True)
