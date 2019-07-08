from flask import render_template, redirect, url_for
from flask_login import current_user, login_user

from app import app
from forms import LoginForm
from models import User, Playground


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    
    if form.validate_on_submit():
        user = User.query.filter_by(login=form.login.data, password=form.password.data).first()
        if user is not None:
            print("hello, ", form.login.data)
            login_user(user, remember=True)
            return redirect(url_for("index"))
    
    return render_template("login.html", form=form)


@app.route("/b_<page>")
def basketball(page):
    page = int(page)    
    playgrounds = Playground.query.filter_by(playground_type="b").all()[page*9:page*9+9]
    
    return render_template("basketball.html", playgrounds=playgrounds, page=int(page))


if __name__ == "__main__":
    app.run()