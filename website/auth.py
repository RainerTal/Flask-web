from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
import bcrypt
from . import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user:
            if bcrypt.checkpw(password.encode('utf-8'), user.password.encode('utf-8')):
                flash('Logged in successfully', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
            else:
                flash('Incorrect password', category='error')
        else:
            flash('That email does not exist', category='error')

    data = request.form
    return render_template("login.html", user=current_user)

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

@auth.route('/sign-up', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        email = request.form.get("email")
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        user = User.query.filter_by(email=email).first()
        if user:
            flash('That email already exists', category='error')
        elif len(first_name) < 2:
            flash("Name is shorter than 2 characters", category="error")
        elif password1 != password2:
            flash("Passwords do not match", category="error")
        elif len(password1) < 7 or not any(char.isdigit() for char in password1):
            flash("Password must be at least 7 characters long and contain a number", category="error")
        else:
            hashed_password = bcrypt.hashpw(password1.encode('utf-8'), bcrypt.gensalt())
            new_user = User(email=email, first_name=first_name, password=hashed_password.decode('utf-8'))
            db.session.add(new_user)
            db.session.commit()
            login_user(user, remember=True)
            flash("Account created", category="success")
            return redirect(url_for('views.home'))
        
        def verify_user_password(stored_hash, password):
            return bcrypt.checkpw(password.encode('utf-8'), stored_hash.encode('utf-8'))
            
    return render_template("sign_up.html", user=current_user)

@auth.route("/stock")
def stock():
    return render_template("stock.html", user = current_user)