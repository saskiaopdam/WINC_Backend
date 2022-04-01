from flask import Flask

__winc_id__ = "cc1b724762854e85a8defa04287f708b"
__human_name__ = "requests"

app = Flask(__name__)


# @app.route("/")
# def hello_world():
#     return "<p>Hello, World!</p>"

@app.route("/")
def index():
    return "<p>Home, sweet home.</p>"


@app.route("/greet/")
@app.route("/greet/<name>")
def greet(name=None):
    if name:
        return f"<h1>Hello, {name}!</h1>"
    else:
        return f"<h1>Hello, world!</h1>"
