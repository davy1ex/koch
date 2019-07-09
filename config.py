import os


class Config:
    DEBUG = True
    SECRET_KEY = os.urandom(32)
    WTF_CSRF_SECRET_KEY = os.urandom(64)
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "sqlite:///test.db"
