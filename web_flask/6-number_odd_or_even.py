#!/usr/bin/python3
"""Flask"""
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return a given string"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Returns a given string"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """display C followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text="is cool"):
    """display Python followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """display “n is a number” only if n is an integer"""
    if isinstance(n, int):
        return "{} is a number".format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """display a HTML page only if n is an integer"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """display a HTML page only if n is an integer:
    H1 tag: “Number: n is even | odd” inside the tag BODY
    """
    if isinstance(n, int):
        o_or_e = "odd" if n % 2 != 0 else "even"
        return render_template("6-number_odd_or_even.html", n=n, o_or_e=o_or_e)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
