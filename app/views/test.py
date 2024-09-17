from flask import Blueprint, render_template, redirect, url_for, request, jsonify, send_from_directory, \
    current_app, flash
from werkzeug.utils import secure_filename
import os
from config import Config
from app.models import db, Post

test = Blueprint("test", __name__)

@test.route("/test")
def index():
    return render_template("test.html")
