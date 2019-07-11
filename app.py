import os.path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
# 
from flask_admin import form
import random
import os
#
from flask_admin.form.upload import FileUploadField


from config import Config


app = Flask(__name__)
app.config.from_object(Config)

db = SQLAlchemy(app)

login = LoginManager(app)

from models import Playground
admin = Admin(app)


def prefix_name(obj, file_data):
    parts = os.path.splitext(file_data.filename)
    return secure_filename("file-%s%s" % parts)


class MicroBlogModelView(ModelView):
    form_extra_fields = {
        "photo": form.FileUploadField("photo", base_path="static/img")
    }

    def _change_path_data(self, _form):
        try:
            storage_file = _form.file.data

            if storage_file is not None:
                hash = random.getrandbits(64)
                ext =storage_file.filename.split(".")[-1]
                path = "%s.%s" % (hash, ext)

                print(path)

                storage_file_save(os.path.join(app.config["STORAGE"], path))
                _form.photo.data = path

                del _form.file
        except Exception as ex:
            pass

        return _form

    def edit_form(self, obj=None):
        return self._change_path_data(super(MicroBlogModelView, self).edit_form(obj))
    
    
    def create_form(self, obj=None):
        return self._change_path_data(super(MicroBlogModelView, self).create_form(obj))


admin.add_view(MicroBlogModelView(Playground, db.session))