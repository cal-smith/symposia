from bottle import *
from models import user, categories, posts
import json

@view('index')
def index():#list all categories(GET)
	cat = categories.all()
	return dict(name=json.dumps(cat))

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

@view('user')
def users(name):
	info = user.info(name)
	print info
	return dict(data=json.dumps(info))