from flask import Blueprint

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return('<p>Login</p>')

@auth.route('/logout')
def logout():
    return('<p>Logout</p>')

@auth.route('/sign-up')
def signup():
    return('<p>Sign Up</p>')

@auth.route("/stock")
def stock():
    return('<p>Stock</p>')