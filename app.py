from flask import render_template
from flask_login import login_required, current_user

from app import create_app
from app.extensions import login_manager

app = create_app()


@login_manager.user_loader
def load_user(user_id):
    from app.models.user import User
    return User.get_by_id(user_id)


@app.route("/")
def home():
    return render_template("login.html")


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template(
        "dashboard.html",
        current_user=current_user
    )


if __name__ == "__main__":
    app.run(debug=True)