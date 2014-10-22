from models import Session
from tables import Posts, Replies, Users
from uuid import uuid4
session = Session()

def all(category):
	res = []
	for row in session.query(Posts).filter(Posts.category == category).limit(25):
		res.append({'title': row.title, 'md':row.md})
	return res

def post(postid, category):
	op = session.query(Posts, Users).\
		filter(Users.id == Posts.userid).\
		filter(Posts.postid == postid, Posts.category == category).first()
	print 'test', op[0].postid
	res = {'title': op[0].title, 
			'md': op[0].md, 
			'html': op[0].html, 
			'userid': op[1].id,
			'username': op[1].username,
			'replies': []}
	for reply, user in session.query(Replies, Users).\
				filter(Users.id == Replies.userid).\
				filter(Replies.postid == postid).limit(25):
		res['replies'].append({'md': reply.md, 
								'html': reply.html,
								'userid': user.id,
								'username': user.username})
	return res

def next(postid, category, next=True):
	if next:
		#next post as ordered by date
		op = session.query(Posts, Users).\
			filter(Users.id == Posts.userid).\
			filter(Posts.postid == postid, Posts.category == category).first()#.next()?
		print 'test', op[0].postid
		#postid = w/e the next postid is
		res = {'title': op[0].title, 
			'md': op[0].md, 
			'html': op[0].html, 
			'userid': op[1].id,
			'username': op[1].username,
			'replies': []}
		for reply, user in session.query(Replies, Users).\
					filter(Users.id == Replies.userid).\
					filter(Replies.postid == postid).limit(25):
			res['replies'].append({'md': reply.md, 
									'html': reply.html,
									'userid': user.id,
									'username': user.username})
		return res
	else:
		#previous post as orderd by date
		pass

def add(userid, title, md, category):
	postid = str(uuid4())
	post = Posts(postid=postid, userid=userid, title=title, md=md, category=category)#html, posted
	session.add(post)
	session.commit()
	return True

def reply(userid, postid, md):
	replyid = str(uuid4())
	reply = Replies(replyid=replyid, postid=postid, userid=userid, md=md)#html, posted
	session.add(reply)
	session.commit()
	return True

def move(postid, newcat):
	session.query(Posts).filter(Posts.postid == postid).update({Posts.category: newcat})
	session.commit()
	return True

def delete(postid):
	session.query(Posts).filter(Posts.postid == postid).delete()
	session.query(Replies).filter(Replies.postid == postid).delete()
	return True



