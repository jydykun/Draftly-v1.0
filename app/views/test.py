from flask import Blueprint, render_template, redirect, url_for, request, jsonify, send_from_directory, \
    current_app, flash
from werkzeug.utils import secure_filename
import os
from config import Config
from app.models import db, Post
from flask_wtf import FlaskForm
from wtforms import EmailField
from wtforms.validators import Email, DataRequired

class TestForm(FlaskForm):
    email = EmailField("Email", validators=[DataRequired(), Email(check_deliverability=True)])


test = Blueprint("test", __name__)

@test.route("/test", methods=["GET", "POST"])
def index():

    form = TestForm()


    return render_template("test.html", form=form)
