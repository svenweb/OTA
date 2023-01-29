
from flask_sqlalchemy import SQLAlchemy

from flask_login import UserMixin

from sqlalchemy.orm import relationship
from flask_dance.consumer.storage.sqla import OAuthConsumerMixin

from apps import db, login_manager

from apps.authentication.util import hash_pass
from sqlalchemy import Column, Integer, String, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime


Base = declarative_base()


class Users(db.Model, UserMixin):

    __tablename__ = 'Users'

    id            = db.Column(db.Integer, primary_key=True)
    username      = db.Column(db.String(64), unique=True)
    email         = db.Column(db.String(64), unique=True)
    password      = db.Column(db.LargeBinary)

    oauth_github  = db.Column(db.String(100), nullable=True)

    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)

    def __repr__(self):
        return str(self.username) 



class Post(db.Model):
    __tablename__ = 'Posts'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False, default="Title")
    price = db.Column(db.Float, nullable=False, default=100.0)
    type = db.Column(db.String(100), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.id'), nullable=False)
    images = db.relationship('Image', backref='post', lazy=True)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow, autoincrement=True)

class Bicycle(Post):
    __tablename__ = 'Bicycles'
    year = db.Column(db.Integer, nullable=False)
    make = db.Column(db.String(100), nullable=False)
    model = db.Column(db.String(100), nullable=False)
    bike_type = db.Column(db.String(100), nullable=False)
    frame_material = db.Column(db.String(100), nullable=False)
    frame_size = db.Column(db.String(100), nullable=False)
    suspension = db.Column(db.String(100), nullable=False)
    front_travel = db.Column(db.String(100), nullable=False)
    rear_travel = db.Column(db.String(100), nullable=False)
    brake_type = db.Column(db.String(100), nullable=False)
    handlebar_type = db.Column(db.String(100), nullable=False)
    e_assist = db.Column(db.String(100), nullable=False)
    wheel_size = db.Column(db.String(100), nullable=False)
    condition = db.Column(db.String(100), nullable=False)

class BicyclePart(Post):
    __tablename__ = 'Bicycle_Parts'
    id = db.Column(db.Integer, db.ForeignKey('Posts.id'), primary_key=True)

class Image(db.Model):
    __tablename__ = 'Images'
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(200), nullable=False)
    post_id = db.Column(db.Integer, db.ForeignKey('Posts.id'), nullable=False)


@login_manager.user_loader
def user_loader(id):
    return Users.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    username = request.form.get('username')
    user = Users.query.filter_by(username=username).first()
    return user if user else None

class OAuth(OAuthConsumerMixin, db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey("Users.id", ondelete="cascade"), nullable=False)
    user = db.relationship(Users)
