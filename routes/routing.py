from bottle import *
import main, posts

def routing(app):
	app.route('/', 'GET', main.index)
	app.route('/new/', 'POST', posts.new_category)
	app.route('/new', 'POST', posts.new_category)
	app.route('/login/', 'GET', main.login)
	app.route('/login/', 'POST', main.do_login)
	app.route('/login', 'POST', main.do_login)
	app.route('/register/', 'POST', main.register)
	app.route('/register', 'POST', main.register)
	app.route('/user/<name>/', 'GET', main.users)
	app.route('/user/<name>', 'GET', main.users)
	app.route('/<category>/', 'GET', posts.category)
	app.route('/<category>', 'GET', posts.category)
	app.route('/<category>/<post>/', 'GET', posts.post)
	app.route('/<category>/<post>', 'GET', posts.post)
	app.route('/<category>/<post>/<next>/', 'GET', posts.next_post)
	app.route('/<category>/<post>/<next>', 'GET', posts.next_post)
	app.route('/<category>/new/', 'POST', posts.new_post)
	app.route('/<category>/new', 'POST', posts.new_post)

app = Bottle()

routing(app)