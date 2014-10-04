from models import Session
from tables import Users
session = Session()

def add(username, password):
		new_user = Users(id="0", username=username, password=password, created="0", ups="0", downs="0", mode="2")
		session.add(new_user)
		session.commit()

def check():
	pass
