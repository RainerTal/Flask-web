from flask import Blueprint, render_template, request, flash, jsonify, redirect, url_for
from flask_login import login_required, current_user
from .models import Note, CloseValue, OpenValue, OpenValue2, OpenValue3, CloseValue2, CloseValue3, Drink, Drink2
from . import db
import json

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
                    drink_exist = Note.query.filter_by(user_id = current_user.id).first()
                    if drink_exist:
                        flash("You can only add 1 drink at a time, please delete the previous one", category='error')
                    else:
                        new_note = Note(data=note, user_id=current_user.id)
                        db.session.add(new_note)
                        db.session.commit()
                        flash('Drink added!', category='success')
                else:
                    flash('Value requires at least 1 character')
        
                return redirect(url_for('views.home'))
            
        if form_type == 'values_form':
            open_v = request.form.get('open_v')
            close = request.form.get('close')

            if open_v and close:
                try:
                    open_value = float(open_v)
                    close_value = float(close)

                    new_open_value = OpenValue(data=open_value, user_id=current_user.id)               
                    new_close_value = CloseValue(data=close_value, user_id=current_user.id)

                    db.session.add(new_open_value)
                    db.session.add(new_close_value)

                    db.session.commit()
                        
                    flash('Values added successfully!', category='success')
                except ValueError:
                    flash('One or more values are not valid numbers', category='error')          
    
            else:
                flash('Please fill in all fields', category='error')

        if form_type == 'drink_form':
            drink = request.form.get('drink')
            if drink:
                if len(drink) > 0:
                    drink_exist = Drink.query.filter_by(user_id = current_user.id).first()
                    if drink_exist:
                        flash("You can only add 1 drink at a time, please delete the previous one", category='error')
                    else:
                        new_drink = Drink(data=drink, user_id=current_user.id)
                        db.session.add(new_drink)
                        db.session.commit()
                        flash('Drink added!', category='success')
                else:
                    flash('Value insert requires at least 1 character', category='error')
        
                return redirect(url_for('views.home'))
            

        if form_type == 'values_form2':
            open_v2 = request.form.get('open_v2')
            close2 = request.form.get('close2')

            if open_v2 and close2:
                try:
                    open_v2 = float(open_v2)
                    close2 = float(close2)

                    new_open_value2 = OpenValue2(data=open_v2, user_id=current_user.id)
                    new_close_value2 = CloseValue2(data=close2, user_id=current_user.id)

                    db.session.add(new_open_value2)
                    db.session.add(new_close_value2)
                    db.session.commit()

                    flash('Values added successfully!', category='success')
                except ValueError:
                    flash('One or more values are not valid numbers', category='error')     
            else:
                flash("Please fill in all fields", category='error')  

        if form_type == 'drink_form2':
            drink2 = request.form.get('drink2')
            if drink2:
                if len(drink2) > 0:
                    drink_exist = Drink2.query.filter_by(user_id = current_user.id).first()
                    if drink_exist:
                        flash("You can only add 1 drink at a time, please delete the previous one", category='error')
                    else:
                        new_drink2 = Drink2(data=drink2, user_id=current_user.id)
                        db.session.add(new_drink2)
                        db.session.commit()
                        flash('Drink added!', category='success')
                else:
                    flash('Value insert requires at least 1 character')
        
                return redirect(url_for('views.home'))   

        if form_type == 'values_form3':
            open_v3 = request.form.get('open_v3')
            close3 = request.form.get('close3')

            if open_v3 and close3:
                try:
                    open_v3 = float(open_v3)
                    close3 = float(close3)

                    new_open_value3 = OpenValue3(data=open_v3, user_id=current_user.id)
                    new_close_value3 = CloseValue3(data=close3, user_id=current_user.id)

                    db.session.add(new_open_value3)
                    db.session.add(new_close_value3)
                    db.session.commit()

                    flash('Values added successfully!', category='success')
                except ValueError:
                    flash('One or more values are not valid numbers', category='error')     
            else:
                flash("Please fill in all fields", category='error')  


    return render_template("home.html", user=current_user, zip=zip)

@views.route('/delete-note', methods=['POST'])
@login_required
def delete_note():
    note = json.loads(request.data)
    noteId = note['noteId']
    note = Note.query.get(noteId)
    if note:
        if note.user_id == current_user.id:
            db.session.delete(note)
            db.session.commit()
    return jsonify({})

@views.route('/delete-drink', methods=['POST'])
@login_required
def delete_drink():
    drink = json.loads(request.data)
    drinkId = drink['drinkId']
    drink = Drink.query.get(drinkId)
    if drink:
        if drink.user_id == current_user.id:
            db.session.delete(drink)
            db.session.commit()
    return jsonify({})

@views.route('/delete-drink2', methods=['POST'])
@login_required
def delete_drink2():
    drink2 = json.loads(request.data)
    drink2Id = drink2['drink2Id']
    drink2 = Drink2.query.get(drink2Id)
    if drink2:
        if drink2.user_id == current_user.id:
            db.session.delete(drink2)
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

    db.session.commit()  
    return jsonify({})

@views.route('/delete-values2', methods=['POST'])
@login_required
def delete_values2():
    data = json.loads(request.data)

    open_v2Id = data['open_v2Id']
    if open_v2Id:
        open_v2 = OpenValue2.query.get(open_v2Id)
        if open_v2 and open_v2.user_id == current_user.id:
            db.session.delete(open_v2)

    close2Id = data['close2Id']
    if close2Id:
        close2 = CloseValue2.query.get(close2Id)
        if close2 and close2.user_id == current_user.id:
            db.session.delete(close2)

    db.session.commit()  
    return jsonify({})

@views.route('/delete-values3', methods=['POST'])
@login_required
def delete_values3():
    data = json.loads(request.data)

    open_v3Id = data['open_v3Id']
    if open_v3Id:
        open_v3 = OpenValue3.query.get(open_v3Id)
        if open_v3 and open_v3.user_id == current_user.id:
            db.session.delete(open_v3)

    close3Id = data['close3Id']
    if close3Id:
        close3 = CloseValue3.query.get(close3Id)
        if close3 and close3.user_id == current_user.id:
            db.session.delete(close3)

    db.session.commit()  
    return jsonify({})

@views.route('/stock')
@login_required
def stock():
    return render_template('stock.html', user = current_user)

@views.route('/chart-data', methods=['GET'])
@login_required
def chart_data():
    open_values = OpenValue.query.filter_by(user_id=current_user.id).all()
    close_values = CloseValue.query.filter_by(user_id=current_user.id).all()

    num_values = min(len(open_values), len(close_values))

    data = []
    for i in range(num_values):
        data.append({
            'x': int(close_values[i].date.timestamp() * 1000),  
            'y': [
                open_values[i].data,
                open_values[i].data,
                close_values[i].data,
                close_values[i].data,
            ]
        })

    return jsonify(data)

@views.route('/chart-data2', methods=['GET'])
@login_required
def chart_data2():
    open_values2 = OpenValue2.query.filter_by(user_id=current_user.id).all()
    close_values2 = CloseValue2.query.filter_by(user_id=current_user.id).all()

    numerical_values = min(len(open_values2), len(close_values2))

    data2 = []
    for i in range(numerical_values):
        data2.append({
            'x': int(close_values2[i].date.timestamp() * 1000),
            'y': [
                open_values2[i].data,
                open_values2[i].data,
                close_values2[i].data,
                close_values2[i].data,
            ]
        })

    return jsonify(data2)

@views.route('/chart-data3', methods=['GET'])
@login_required
def chart_data3():
    open_values3 = OpenValue3.query.filter_by(user_id=current_user.id).all()
    close_values3 = CloseValue3.query.filter_by(user_id=current_user.id).all()

    numerical_values = min(len(open_values3), len(close_values3))

    data3 = []
    for i in range(numerical_values):
        data3.append({
            'x': int(close_values3[i].date.timestamp() * 1000),
            'y': [
                open_values3[i].data,
                open_values3[i].data,
                close_values3[i].data,
                close_values3[i].data,
            ]
        })

    return jsonify(data3)


@views.route('/chart-name', methods=['GET'])
@login_required
def chart_name():
    notes = Note.query.filter_by(user_id=current_user.id).all()

    notes_data = [note.data for note in notes]

    return jsonify(notes_data)

@views.route('/chart-name2', methods=['GET'])
@login_required
def chart_name2():
    drinks = Drink.query.filter_by(user_id=current_user.id).all()

    drinks_data = [drink.data for drink in drinks]

    return jsonify(drinks_data)

@views.route('/chart-name3', methods=['GET'])
@login_required
def chart_name3():
    drinks2 = Drink2.query.filter_by(user_id=current_user.id).all()

    drinks_data2 = [drink2.data for drink2 in drinks2]

    return jsonify(drinks_data2)