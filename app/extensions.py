from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_pymongo import PyMongo

bcrypt = Bcrypt()
mongo = PyMongo()
login_manager = LoginManager()

login_manager.login_view = "auth.login"
login_manager.login_message = "Please login first."
login_manager.login_message_category = "warning"