from flask import Flask, render_template, redirect, url_for
# from sys import os

__winc_id__ = "9263bbfddbeb4a0397de231a1e33240a"
__human_name__ = "templates"

app = Flask(__name__)


# @app.route("/")
# def index():
#     return "This is an empty Flask project that you need to work on."


# @app.route("/home")
# def home():
#     return redirect(url_for('index'), code=302)
@app.route("/home")
def home():
    return redirect('http://127.0.0.1:5000/')


@app.route("/")
def index():
    return render_template('index.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/extra')
def extra():
    return render_template('extra.html')


# if __name__ == '__main__':
#     # Bind to PORT if defined, otherwise default to 5000.
#     port = int(os.environ.get('PORT', 5000))
#     app.run(host='0.0.0.0', port=port)
