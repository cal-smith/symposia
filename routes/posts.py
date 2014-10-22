from bottle import *
from models import user, categories, posts
import json

def new_category():#add a category (move to routes/admin.py?)(POST)
	name = request.query.name
	description = request.query.description
	categories.add(name, description)
	return 'True'

def category(category):#get all posts from a category(GET)
	post = posts.all(category)
	return template('{{category}}', category=json.dumps(post))

def post(category, post):#get op and replys from a category(GET)
	post = posts.post(post, category)
	return template('{{post}}', post=json.dumps(post))

def next_post(category, post, next):
	if next == "next":
		post = posts.next(post, category)
		return template('{{post}}', post=json.dumps(post))
	elif next == "last":
		post = posts.next(post, category, False)
		return template('{{post}}', post=json.dumps(post))

def new_post(category):#add post to category(POST)
	title = request.query.title
	md = request.query.md
	userid = 0 #user.userid
	posts.add(userid, title, md, category)
	return 'True'