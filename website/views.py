from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
from .models import Collection #add Card
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
            print(new_collection)
            db.session.commit()
            
            flash('Collection Added', category='success')
        else:
            flash('Name is too short', category='error')
        
    return render_template('home.html', user=current_user)


@views.route('/', methods=['GET', 'POST'])
def started_page():
    return render_template('started_page.html', user=None)