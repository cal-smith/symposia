from bottle import *

app = Bottle()

@app.get('/')
def index():
	return '<p>Hello</p>'

@app.get('/<category>')
def category(category):
	return template('{{category}}', category=category)

@app.post('/<category>')
def new_category(category):
	return template('{{category}}', category=category)

@app.get('/<category>/<post>')
def post(post):
	return template('{{post}}', post=post)

@app.post('/<category>/<post>')
def new_post(post):
	return template('{{post}}', post=post)

@app.get('/login')
def login():
	pass

@app.post('/login')
def do_login():
	pass

@app.post('/register')
def register():
	pass