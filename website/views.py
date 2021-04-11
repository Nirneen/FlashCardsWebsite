from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json 


views = Blueprint('views', __name__)

@views.route('/home', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        new_collection = request.form.get('new_collection')
        print(new_collection)
    return render_template('home.html', user=current_user)


@views.route('/', methods=['GET', 'POST'])
def started_page():
    return render_template('started_page.html', user=None)