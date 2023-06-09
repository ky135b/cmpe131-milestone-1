### IF THIS FILE IS MODIFIED, RUN tables.py TO RECREATE TABLES
from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(32), nullable=False)
    password = db.Column(db.String(32), nullable=False)
    email = db.Column(db.String(32), nullable=False)

    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def __repr__(self):
        return f'<user {self.id}: {self.username}>'

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(256))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post {self.id}: {self.body}>'

class Group(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    groupname = db.Column(db.String(26), nullable=False)
    username = db.Column(db.String(32), nullable=False)
    def __repr__(self):
        return f'<Group {self.id}: {self.groupname}>'

class GroupMember(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    groupid = db.Column(db.Integer, nullable=False)
    memberemail = db.Column(db.String(32), nullable=False)
    def __repr__(self):
        return f'<GroupMember {self.groupname}: {self.memberemail}>'

class TodoItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(200))
    completed = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(32), nullable=False)
    
    def __repr__(self):
        return f'<TodoItem {self.id}: {self.content} {self.completed}>'
class Email(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   recipient = db.Column(db.String(32), nullable = False)
   subject = db.Column(db.String(32), nullable = False)
   body = db.Column(db.String(200), nullable = False)
   sender = db.Column(db.String(32), nullable =False)
   file = db.Column(db.String(50), nullable = False)
   data = db.Column(db.LargeBinary, nullable = False)
   urgent = db.Column(db.Integer, nullable=False)
   def __repr__(self):
        return f'<Email {self.id}: {self.subject} {self.body}>'

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
