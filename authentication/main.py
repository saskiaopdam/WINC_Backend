import os

from flask import Flask, redirect, render_template, request, session, url_for
from helpers import valid_login

__winc_id__ = "8fd255f5fe5e40dcb1995184eaa26116"
__human_name__ = "authentication"

app = Flask(__name__)

app.secret_key = os.urandom(16)


@app.route("/home")
def redirect_index():
    return redirect(url_for("index"))


@app.route("/")
def index():
    return render_template("index.html", title="Index")


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/lon")
def lon():
    return render_template("lon.html", title="League of Nations")


@app.route("/login", methods=["GET", "POST"])
def login():
    # YOUR SOLUTION HERE
    error = None
    # if form is submitted
    if request.method == "POST":
        # record user name and password
        session["username"] = request.form["username"]
        session["password"] = request.form["password"]

        print(session["username"])
        print(session["password"])

        # if login is valid
        if valid_login(session["username"], session["password"]):
            # redirect to dashboard
            return redirect("/dashboard")

        # if login not valid
        else:
            error = "Invalid_Login"

            # modify login page with error message - access query parameter ("error") - how?
            # f"/login?error={error}"

            # redirect to login page
            return redirect(f"/login?error={error}")

    # if form is not submitted (GET login page)
    return render_template("login.html", title="Login")


@app.route("/dashboard", methods=["GET", "POST"])
def dashboard():
    # YOUR SOLUTION HERE
    # if form is submitted (Logout button pushed)
    if request.method == "POST":
        # if yes redirect to logout
        return redirect("/logout")

    # if form is not submitted (GET dashboard page)
    return render_template("dashboard.html", title="Dashboard")


# @app.route("/logout", methods=["GET", "POST"])
@app.route("/logout")
def logout():
    # YOUR SOLUTION HERE
    session.pop('username', None)
    return redirect(url_for('index'))
