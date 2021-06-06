#!/usr/bin/python3
# Write a script that starts a Flask web application:
# Importando la libreria flask
from flask import Flask
# Guardando el modulo de la libreria en un variable objeto
app = Flask(__name__)
# Utilizando el modulo route para mostrar un mensaje cuando ingresen a la url
@app.route('/', strict_slashes=False)
def ruta():
    return "Hello HBNB!"
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
