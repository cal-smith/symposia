from models import Session
from tables import Posts
session = Session()

def op():
	pass

def replies():
	pass

def add(userid, title, md, category):
	post = Posts(postid=1, userid=userid, title=title, md=md, category=category)
	session.add(post)
	session.commit()
	return True

def reply():
	pass

def move():
	pass

def delete():
	pass