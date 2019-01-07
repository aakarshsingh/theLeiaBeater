from random import randint

from flask import Flask, jsonify

app = Flask(__name__)

_coordinates = [
    {
        'x': 1,
        'y': 1,
    },
    {
        'x': 2,
        'y': 2,
    },
    {
        'x': 3,
        'y': 3,
    }
]

@app.route('/coordinates')
def get_coordinates():
    return jsonify({'coordinates': _coordinates})

if __name__ == '__main__':
    app.run()
