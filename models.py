from flask_login import UserMixin
from app import login

from app import db


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(128))


class Playground(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    photo = db.Column(db.Unicode(128))
    playground_type = db.Column(db.String(32))
    address = db.Column(db.String(128))
    rating = db.Column(db.Integer)
    description = db.Column(db.String(512))
