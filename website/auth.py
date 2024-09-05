from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    data = request.form
    return render_template("login.html", boolean=True)

@auth.route('/logout')
def logout():
    return('<p>Logout</p>')

@auth.route('/sign-up', methods=["GET", "POST"])
def signup():
    return render_template("sign_up.html")

@auth.route("/stock")
def stock():
    return render_template("stock.html")