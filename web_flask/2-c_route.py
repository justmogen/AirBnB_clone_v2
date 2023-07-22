#!/usr/bin/python3
""" Starts a Flask web application listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")

# route to display "Hello HBNB"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return Hello HBNB"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Returns HBNB"""
    return ("HBNB")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
