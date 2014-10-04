from models import Session, engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
Base = declarative_base()
class Users(Base):
	__tablename__ = 'users'

	id = Column(String, primary_key=True)
	username = Column(String)
	password = Column(String)
	created = Column(String)
	ups = Column(Integer)
	downs = Column(Integer)
	mode = Column(Integer)

class Posts(Base):
	__tablename__ = "posts"

	postid = Column(String, primary_key=True)
	category = Column(String)
	userid = Column(String)
	title = Column(String)
	md = Column(String)
	html = Column(String)
	posted = Column(String)

class Replies(Base):
	__tablename__ = "replies"

	replyid = Column(String, primary_key=True)
	postid = Column(String)
	userid = Column(String)
	md = Column(String)
	html = Column(String)
	posted = Column(String)

class Categories(Base):
	__tablename__ = "categories"

	name = Column(String, primary_key=True)
	description = Column(String)

Base.metadata.create_all(engine)