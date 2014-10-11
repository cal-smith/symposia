from bottle import *
from models import user, categories, posts
import json

app = Bottle()

@app.get('/')
@view('index')
def index():
	cat = categories.all()
	return dict(name=json.dumps(cat))

@app.post('/new')
def new_category():
	name = request.query.name
	description = request.query.description
	categories.add(name, description)
	return 'True'

@app.get('/<category>')
def category(category):
	post = categories.posts(category)
	return template('{{category}}', category=json.dumps(post))

@app.post('/<category>/new')
def new_post(category):
	title = request.query.title
	md = request.query.md
	userid = 0 #user.userid
	posts.add(userid, title, md, category)
	return 'True'

@app.get('/<category>/<post>')
def post(post):
	return template('{{post}}', post=post)

@app.get('/login')
def login():
	pass

@app.post('/login')
def do_login():
	pass
	redirect('/')

@app.post('/register')
def register():
	pass