from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

login = LoginManager(app)

from models import Playground
admin = Admin(app)
admin.add_view(ModelView(Playground, db.session))