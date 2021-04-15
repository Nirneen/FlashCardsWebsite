from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Collection, Card #add Card
import json 


views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        input_collection = str(request.form.get('new_collection'))
        
        if len(input_collection) >= 1:
            new_collection = Collection(user_id=current_user.id, collection_name=input_collection)
            db.session.add(new_collection)
            db.session.commit()
            
            flash('Collection Added', category='success')

        else:
            flash('Name is too short', category='error')
        
    return render_template('home.html', user=current_user)


@views.route('/', methods=['GET', 'POST'])
def started_page():
    return render_template('started_page.html', user=None)

@views.route('/collection/<int:id>', methods=['GET', 'POST'])
@login_required
def collection(id):#/blog/<int:id>
    collection= Collection.query.filter_by(id=id).first_or_404()
    #serialized_collection = collection.serialize
    if request.method == 'POST':
        input_front_side = request.form.get('new_card_front_side')
        input_back_side = request.form.get('new_card_back_side')

        if (len(input_front_side) + len(input_back_side)) > 1:
            new_card = Card(collection_id=id, front_side=input_front_side, back_side=input_back_side)
            db.session.add(new_card)
            print(new_card.back_side)
            db.session.commit()


    return render_template('collection.html', user=current_user, collection=collection) 
    