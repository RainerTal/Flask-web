from flask import Blueprint, render_template, request, flash

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
    if request.method == 'POST':
        email = request.form.get("email")
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(firstName) < 2:
            flash("Name is shorter than 2 characters", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        elif len(password1) < 7 or not any(char.isdigit() for char in password1):
            flash("Password must be at least 7 characters long and contain a number", category="error")
        else:
            flash("Account created", category="success")

    return render_template("sign_up.html")

@auth.route("/stock")
def stock():
    return render_template("stock.html")