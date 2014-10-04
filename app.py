from bottle import *
from routes import main
from models import user, categories, posts

root = Bottle()
@root.route('/<file>')
def static(file):
	return static_file(file, root='static')
root.merge(main.app)

root.run(host='localhost', port=8888)