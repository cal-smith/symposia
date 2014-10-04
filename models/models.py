from sqlalchemy import create_engine
engine = create_engine('postgresql://localhost/forum2', echo=True)
#'postgresql://scott:tiger@localhost/mydatabase'
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

from sqlalchemy import Column, Integer, String

test = "a"

class User(Base):
	__tablename__ = 'users'

	id = Column(String, primary_key=True)
	username = Column(String)
	password = Column(String)
	created = Column(String)
	ups = Column(Integer)
	downs = Column(Integer)
	mode = Column(Integer)

	def __reper__(self):
		pass

	def check(self):
		pass

	def add(self):
		pass

class Posts(object):
	def __init__(self, arg):
		super(Posts, self).__init__()
		self.arg = arg

	def op(self):
		pass

	def replies(self):
		pass

	def add(self):
		pass

	def reply(self):
		pass

	def move(self):
		pass

	def delete(self):
		pass
		
class Categories(object):
	def __init__(self, arg):
		super(Categories, self).__init__()
		self.arg = arg

	def all(self):
		pass

	def posts(self):
		pass
	
	def info(self):
		pass

	def add(self):
		pass

	def delete(self):
		pass

	def edit(self):
		pass