from bottle import *
#from routes import main
from routes import routing

root = Bottle()
@root.route('/<file>')
def static(file):
	return static_file(file, root='static')
root.merge(routing.app)

root.run(host='localhost', port=8888)