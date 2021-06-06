#!/usr/bin/python3
"""importando la libreria flask"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def helloHbnb():
    return "Hello HBNB!"

"""condicion"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
