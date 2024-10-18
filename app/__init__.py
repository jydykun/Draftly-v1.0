from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from config import Config
from app.models import db, User

login_manager = LoginManager()
login_manager.login_view = "auth.login"
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        return db.session.get(User, user_id)

    # Register Blueprints
    from app.views.main import main
    app.register_blueprint(main)

    from app.views.auth import auth
    app.register_blueprint(auth)

    return app