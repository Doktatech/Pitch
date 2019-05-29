from datetime import datetime
from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from flask_login import UserMixin
from . import login_manager


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(UserMixin, db.Model):
    '''
    Class that defines a user object and commits to a database
    '''
    __tablename__ = 'users'
    id = db.Column(db.Integer,  primary_key = True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True, index =True)
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    pass_secure = db.Column(db.String(255))

    pitchs = db.relationship('Pitch',backref='user',lazy='dynamic')
    comments = db.relationship('Comment', backref = 'comment', lazy= "dynamic")

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.pass_secure = generate_password_hash(password)


    def verify_password(self,password):
        return check_password_hash(self.pass_secure,password)

    def __repr__(self):
        return f'{self.username}'

class Pitch(db.Model):
    '''
    Class that define  a new object (pitch ) and commits it into a database
    '''
    __tablename__ = 'pitch'

    id = db.Column(db.Integer,primary_key = True)
    title = db.Column(db.String(255))
    content = db.Column(db.String())
    category = db.Column(db.String(255))
    
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    pitch_id = db.relationship('Comment', backref = 'comments', lazy= "dynamic")

    def __repr__(self):
        return f'{self.title}'

class Comment(db.Model):
    '''
    Class for thhe comment object
    '''
    __tablename__='comments'

    id = db.Column(db.Integer,primary_key=True)
    comment_content = db.Column(db.String())
    pitch_id = db.Column(db.Integer,db.ForeignKey('pitch.id'))
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))


    def __repr__(self):
        return f'{self.comment}'  



