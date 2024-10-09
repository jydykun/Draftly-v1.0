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

my_choices = [(1, "One"), (2, "Two"), (3, "Three")]

def selectTesting(field, **kwargs):
    field_id = field.id
    field_name = field.name
    html = [f"<select {html_params(id=field_id, name=field_name)}>"]

    # Iterate through choices and generate option tags
    for value, name, selected, render_kw in field.iter_choices():
        option_html = f"<option {html_params(value=value, **render_kw)}"
        if selected:
            option_html += " selected"
        option_html += f">{name}</option>"
        html.append(option_html)

    html.append("</select>")
    return "".join(html)

class TestForm(FlaskForm):
    tester = SelectField("Tester", choices=my_choices, widget=selectTesting)



test = Blueprint("test", __name__)

@test.route("/test")
def index():

    form = TestForm()


    return render_template("test.html", form=form)
