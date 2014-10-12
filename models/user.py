from models import Session
from tables import Users
from uuid import uuid4
from datetime import date
import bcrypt
session = Session()

def add(username, password):
		id = str(uuid4())
		password = bcrypt.hashpw(password, bcrypt.gensalt())
		created = date.today()
		new_user = Users(id=id, username=username, password=password, created=created, ups="0", downs="0", mode="0")
		session.add(new_user)
		session.commit()
		return True #user added

def check(username, password):
	user = session.query(Users).filter(Users.username == username).first()
	if user.username == username and bcrypt.hashpw(password, user.password) == user.password:
		#set session, return user details etc
		return True
	else:
		#return some kind of error: {error: username or password blah blah}
		return False

def info():
	#userid, tokens, other things
	pass

def ban():
	#so yeah we kinda need this
	#'muted (can't post)', 'login ban (can't login)', 'ip ban' (can't even visit the site [from a specific ip and/or other ident info])
	pass

def delete():
	#for admins and users alike
	pass