from flask import Flask

from app.routes.auth import auth_bp
from app.utils.password import bcrypt

app = Flask(__name__)

app.secret_key = "SkinAI@2026"

bcrypt.init_app(app)

app.register_blueprint(auth_bp)


@app.route("/")
def home():
    return "Skin Care AI"


@app.route("/dashboard")
def dashboard():
    return "Dashboard"


if __name__ == "__main__":
    app.run(debug=True)