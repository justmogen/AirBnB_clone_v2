#!/usr/bin/python3
"""Starting a flask web application listening on 0.0.0.0, port 5000
"""

from flask import Flask

app = Flask("__name__")

# Route to display "Hello HBNB!"
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Return a -Hello HBNB-"""
    return ("Hello HBNB!")


if __name__ == "__main__":
    # Run the Flask application on 0.0.0.0, port 5000
    app.run(host="0.0.0.0", port=5000)
