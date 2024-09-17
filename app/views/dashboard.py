from flask import Blueprint, render_template

dashboard = Blueprint("dashboard", __name__)

@dashboard.route("/dashboard")
def test():
    return "Dashboard Page"