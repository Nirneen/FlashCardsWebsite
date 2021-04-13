from . import db #from website import db
from flask_login import UserMixin
from sqlalchemy import func


class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	email = db.Column(db.String(150), unique=True)
	password = db.Column(db.String(150))
	first_name = db.Column(db.String(150))
	collections = db.relationship('Collection', lazy='dynamic')


class Collection(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))#class User with lower case 
	collection_name = db.Column(db.String(64))
	#cards = db.relationship('Card', lazy='dynamic')

	
'''
class Card(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	collection_id = db.Column(db.Integer, db.ForeignKey('collection.id'))
	front_side = db.Column(db.String(256))
	back_side = db.Column(db.String(256))
'''