from models import Session
from tables import Categories
from sqlalchemy import and_
session = Session()

def all():
	res = []
	for row in session.query(Categories).all():
		res.append({'name': row.name, 'description':row.description})
	return res

def info():
	pass

def add(name, description):
	category = Categories(name=name, description=description)
	session.add(category)
	session.commit()
	return True

def delete():
	pass

def edit():
	pass