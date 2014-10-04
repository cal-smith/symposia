from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
engine = create_engine('postgresql://localhost/forum2', echo=True)
#'postgresql://scott:tiger@localhost/mydatabase'
Session = sessionmaker(bind=engine)