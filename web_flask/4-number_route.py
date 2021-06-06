#!/usr/bin/python3
# importando librerias
from flask import Flask

# obteniendo objeto de la libreria flask
app = Flask(__name__)

# utilizando el modulo route
@app.route('/', strict_slashes=False)
def helloHtn():
    return 'Hello HBNB!'

# Utilizando el modulo route
@app.route('/hbnb', strict_slashes=False)
def helloHbnb():
    return 'HBNB'

#Utilizando el modulo route y escribiendo el valor de la variable pasada como argumento
@app.route('/c/<name>', strict_slashes=False)
def cprofile(name):
    return "C " + str(name)

# Utilizando la funcion route y guardando el valor de una variable por defecto almacenada en una url
@app.route('/python/', defaults={'text':'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def aprofile(text):
    return "Python " + str(text)
    
# Utilizando la funcion route y definiendo el valor de la variable
@app.route('/number/<int:n>', strict_slashes=False)
def vprofile(n):
    return '%d is a number' % n

#

# condicion 
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

