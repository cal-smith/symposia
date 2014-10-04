from bottle import *

root = Bottle()
@root.route('/<file>')
def static(file):
	return static_file(file, root='static')

root.run(host='localhost', port=8080)