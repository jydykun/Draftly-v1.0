from flask import Blueprint, render_template, redirect, url_for, flash, request, session
from flask_login import login_user, current_user, login_required, logout_user
from app.forms import SignupForm, LoginForm
from app.models import db, User
from app import Config

### AUTH BLUEPRINT STARTS HERE ###

auth = Blueprint("auth", __name__)

@auth.context_processor
def inject():
    return {
        "title": Config.APP_NAME,
        "app_name": Config.APP_NAME,
        }


@auth.route("/auth/signup", methods=["GET","POST"])
def signup():
    form = SignupForm()
    if form.validate_on_submit():
        user = User(
            username = form.username.data,
            email = form.email.data,
            )
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()

        # The flash message can only be seen after the request.
        # Therefore, include the get_flashed_messages() function on
        # the redirected page.
        flash("You are now registered!", "success")
        return redirect(url_for("auth.login"))
    
    return render_template("signup.html", form=form)


@auth.route("/auth/login", methods=["GET","POST"])
@auth.route("/login", methods=["GET","POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("main.index"))

    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.scalar(db.select(User).where(User.username == form.username.data))
        if user and user.check_password(form.password.data):
            remember = form.remember_me.data
            login_user(user, remember=remember)
            flash("Login Successful!", "success")
            next = request.args.get("next")
            if next:
                return redirect(next)
            else:
                return redirect(url_for("main.profile", username=current_user.username))
        else:
            flash("Incorrect username or password.", "error")
    return render_template("login.html", form=form)


@auth.route("/auth/logout")
@login_required
def logout():
    logout_user()
    flash("Logged out successfully.")
    return redirect(url_for("auth.login"))