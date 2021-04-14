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
            print(new_collection.collection_name)
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
def get_all_collection(id):#/blog/<int:id>
    collections= Collection.query.filter_by(user_id=current_user.id).all()

    try:
        serialized_collection = collections[id-1].serialize

        return jsonify({"single_collection": serialized_collection}) 
    except Exception as e:#add draw
        print(e)
    