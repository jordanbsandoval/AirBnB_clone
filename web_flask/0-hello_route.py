#!/usr/bin/python3
"""module flask"""
from flask import Flask
app = Flask(__name__)

"""modulo route"""
@app.route('/', strict_slashes=False)
def helloHbnb():
    return "Hello HBNB!"

"""condicion puerto"""
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
