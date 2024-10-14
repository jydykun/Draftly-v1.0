from flask import Blueprint, render_template, redirect, url_for, request, jsonify, send_from_directory, \
    current_app, flash
from werkzeug.utils import secure_filename
import os
from config import Config
from app.models import db, Post
from flask_wtf import FlaskForm
from wtforms import EmailField, SelectField
from wtforms.widgets import html_params, Select
from wtforms.validators import Email, DataRequired

from flask_wtf import FlaskForm
from wtforms import SelectField
from wtforms.widgets import html_params


test = Blueprint("test", __name__)

@test.route("/test")
def index():

    testing = {
        "name":"Joseph",
        "job":"Developer" 
    }

    css = testing.get("age", "default")




    return render_template("test.html", testing=testing, css=css)
