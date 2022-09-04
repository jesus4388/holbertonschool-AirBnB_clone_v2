#!/usr/bin/python3
""" Start a Flask web aplication"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """definition of funtion"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """routes hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def variable(text):
    """routes url variable"""
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python/', defaults={'text': 'is cool'})
@app.route('/python/<text>', strict_slashes=False)
def _python(text):
    """ default value """
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def _integr(n):
    """ is a integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def dis_html(n):
    """display a html if n is a intger"""
    return render_template('5-number.html', title = "HBNB", Number = n)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
