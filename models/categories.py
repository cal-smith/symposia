from models import Session
from tables import Categories, Posts
from sqlalchemy import and_
session = Session()

def all():
	res = []
	for row in session.query(Categories).all():
		res.append({'name': row.name, 'description':row.description})
	return res
		

def posts(category):
	res = []
	for row in session.query(Posts).filter(Posts.category == category).all():
		res.append({'title': row.title, 'md':row.md})
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