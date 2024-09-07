from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, CloseValue, OpenValue, High, Low
from . import db
import json
from decimal import Decimal

views = Blueprint('views', __name__)



@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        note = request.form.get('note')
        if note:
            if len(note) > 0:
                new_note = Note(data=note, user_id=current_user.id)
                db.session.add(new_note)
                db.session.commit()
                flash('Note added!', category='success')
            else:
                flash('Value insert requires at least 1 character')
                
        close = request.form.get('close')
        if close:
            try:
                close_value = float(close)  # Try converting to float
                new_close = CloseValue(data=close_value, user_id=current_user.id)
                db.session.add(new_close)
                db.session.commit()
                flash('Close value added!', category='success')
            except ValueError:
                flash('Value is not a valid float')

    return render_template("home.html", user=current_user)

@views.route('/delete-note', methods=['POST'])
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})



@views.route('/stock')
@login_required
def stock():
    return render_template('stock.html', user = current_user)