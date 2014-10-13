from bottle import *
from models import user, categories, posts
import json

app = Bottle()

@view('index')
def index():#list all categories(GET)
	cat = categories.all()
	return dict(name=json.dumps(cat))

def new_category():#add a category (move to routes/admin.py?)(POST)
	name = request.query.name
	description = request.query.description
	categories.add(name, description)
	return 'True'

def login():#get the login/reg page(GET)
	return template('<p>{{login}}</p>', login='login')

def do_login():#do login(POST)
	#if
	redirect('/')
	#else {error: error details}

def register():#do register(POST)
	#if
	redirect('/')
	#else {error: error details}

def category(category):#get all posts from a category(GET)
	print "this should do nothing on /login"
	post = posts.all(category)
	return template('{{category}}', category=json.dumps(post))

def post(category, post):#get op and replys from a category(GET)
	post = posts.post(post, category)
	return template('{{post}}', post=json.dumps(post))

def new_post(category):#add post to category(POST)
	title = request.query.title
	md = request.query.md
	userid = 0 #user.userid
	posts.add(userid, title, md, category)
	return 'True'

def routing(app):
	app.route('/', 'GET', index)
	app.route('/new', 'POST', new_category)
	app.route('/login', 'GET', login)
	app.route('/login', 'POST', do_login)
	app.route('/register', 'POST', register)
	app.route('/<category>', 'GET', category)
	app.route('/<category>/<post>', 'GET', post)
	app.route('/<category>/new', 'POST', new_post)

routing(app)