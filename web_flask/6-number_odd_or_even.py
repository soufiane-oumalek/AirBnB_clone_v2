#!/usr/bin/python3
"""Starts a Flask web application.

The application listens on 0.0.0.0, port 5000.
Routes:
    /: Displays 'Hello HBNB!'.
    /hbnb: Displays 'HBNB'.
    /c/<text>: displays 'C' followed by the value of text variable 
    /python/(<text>): Displays 'Python' followed by the value of text
    /number/<n>: Displays 'n is a number' only if <n> is an integer.
    /number_template/<n>: Displays an HTML page only if n is an integer.
        - Displays the value of <n> in the body
    /number_odd_or_even/n: Displays an HTML page only if <n> is an integer
    H1 tag: H1 Number: n is even|odd inside the tag BODY
"""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello():
    """ def doc """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ def doc """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ def doc """
    return 'c {}'.format(text.replace("_", " "))


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text):
    """ def doc """
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ def doc """
    return '{} is a number'.format(n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """ def doc """
    if n % 2 == 0:
        c = 'even'
    else:
        c = 'odd'
    return render_template('6-number_odd_or_even.html', number=c, parity=c)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")

