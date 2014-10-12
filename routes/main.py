from bottle import *
from models import user, categories, posts
import json

app = Bottle()

@app.get('/')
@view('index')
def index():#list all categories
	cat = categories.all()
	return dict(name=json.dumps(cat))

@app.post('/new')
def new_category():#add a category (move to routes/admin.py?)
	name = request.query.name
	description = request.query.description
	categories.add(name, description)
	return 'True'

@app.get('/<category>')
def category(category):#get all posts from a category
	post = posts.all(category)
	return template('{{category}}', category=json.dumps(post))

@app.post('/<category>/new')
def new_post(category):#add post to category
	title = request.query.title
	md = request.query.md
	userid = 0 #user.userid
	posts.add(userid, title, md, category)
	return 'True'

@app.get('/<category>/<post>')
def post(category, post):#get op and replys from a category
	post = posts.post(post, category)
	return template('{{post}}', post=json.dumps(post))

@app.get('/login')
def login():#get the login/reg page
	return template('<p>login</p>')

@app.post('/login')
def do_login():#do login
	pass
	#if
	redirect('/')
	#else {error: error details}

@app.post('/register')
def register():#do register
	#if
	redirect('/')
	#else {error: error details}