from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Note, CloseValue, OpenValue, High, Low, User
from . import db
import json
from datetime import datetime

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        form_type = request.form.get('form_type')
        if form_type == 'note_form':
            note = request.form.get('note')
            if note:
                if len(note) > 0:
                    new_note = Note(data=note, user_id=current_user.id)
                    db.session.add(new_note)
                    db.session.commit()
                    flash('Note added!', category='success')
                else:
                    flash('Value insert requires at least 1 character')

        elif form_type == 'values_form':
            open_v = request.form.get('open_v')
            close = request.form.get('close')
            high = request.form.get('high')
            low = request.form.get('low')
            if high >= open_v and low <= close or high >= close and low <= open_v:
                if open_v and close and high and low:
                    try:
                        open_value = float(open_v)
                        close_value = float(close)
                        high_value = float(high)
                        low_value = float(low)

                        new_open_value = OpenValue(data=open_value, user_id=current_user.id)               
                        new_close_value = CloseValue(data=close_value, user_id=current_user.id)
                        new_high_value = High(data=high_value, user_id=current_user.id)
                        new_low_value = Low(data=low_value, user_id=current_user.id)

                        db.session.add(new_open_value)
                        db.session.add(new_close_value)
                        db.session.add(new_high_value)
                        db.session.add(new_low_value)
                        db.session.commit()
                            
                        flash('Values added successfully!', category='success')
                    except ValueError:
                        flash('One or more values are not valid numbers', category='error')            
                else:
                    flash('Please fill in all fields', category='error')
            else:
                flash('High and low values can not be in between open and close values', category='error')

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

@views.route('/delete-values', methods=['POST'])
@login_required
def delete_values():
    data = json.loads(request.data)

    open_vId = data['open_vId']
    if open_vId:
        open_v = OpenValue.query.get(open_vId)
        if open_v and open_v.user_id == current_user.id:
            db.session.delete(open_v)

    closeId = data['closeId']
    if closeId:
        close = CloseValue.query.get(closeId)
        if close and close.user_id == current_user.id:
            db.session.delete(close)

    highId = data['highId']
    if highId:
        high = High.query.get(highId)
        if high and high.user_id == current_user.id:
            db.session.delete(high)

    lowId = data['lowId']
    if lowId:
        low = Low.query.get(lowId)
        if low and low.user_id == current_user.id:
            db.session.delete(low)

    db.session.commit()  
    return jsonify({})

@views.route('/stock')
@login_required
def stock():
    return render_template('stock.html', user = current_user)

@views.route('/chart-data', methods=['GET'])
def chart_data():
    open_values = OpenValue.query.filter_by(user_id=current_user.id).all()
    high_values = High.query.filter_by(user_id=current_user.id).all()
    low_values = Low.query.filter_by(user_id=current_user.id).all()
    close_values = CloseValue.query.filter_by(user_id=current_user.id).all()


    num_values = min(len(open_values), len(high_values), len(low_values), len(close_values))

    data = []
    for i in range(num_values):
        data.append({
            'x': int(close_values[i].date.timestamp() * 1000),  
            'y': [
                open_values[i].data,
                high_values[i].data,
                low_values[i].data,
                close_values[i].data
            ]
        })

    return jsonify(data)