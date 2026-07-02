from flask import Flask

from config import Config
from app.extensions import bcrypt, mongo, login_manager


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    # Initialize Extensions
    bcrypt.init_app(app)
    mongo.init_app(app)
    login_manager.init_app(app)

    # Import Blueprints
    from app.routes.auth import auth_bp
    from app.routes.profile import profile_bp

    # Register Blueprints
    app.register_blueprint(auth_bp)
    app.register_blueprint(profile_bp)

    return app