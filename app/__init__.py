from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_pymongo import PyMongo

from config import Config

# Initialize Extensions
bcrypt = Bcrypt()
mongo = PyMongo()
login_manager = LoginManager()

# Configure Flask-Login
login_manager.login_view = "auth.login"
login_manager.login_message = "Please login first."
login_manager.login_message_category = "warning"


def create_app():
    app = Flask(__name__)

    # Load Configuration
    app.config.from_object(Config)

    # Initialize Extensions
    bcrypt.init_app(app)
    mongo.init_app(app)
    login_manager.init_app(app)

    # Import Blueprints
    from app.routes.auth import auth_bp

    # Register Blueprints
    app.register_blueprint(auth_bp)

    return app