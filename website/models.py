from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(150))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class CloseValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Float)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class OpenValue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Float)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class High(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Float)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class Low(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.Float)
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')
    close_values = db.relationship('CloseValue')
    open_values = db.relationship('OpenValue')
    highs = db.relationship('High')
    lows = db.relationship('Low')


