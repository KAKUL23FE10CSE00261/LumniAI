from flask import Blueprint
from flask import render_template
from flask import request
from flask import redirect
from flask import url_for
from flask import flash

from flask_login import login_user
from flask_login import logout_user

from app.services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)


@auth_bp.route("/signup", methods=["GET", "POST"])
def signup():

    if request.method == "POST":

        success, message = AuthService.register_user(request.form)

        if success:

            flash(message, "success")

            return redirect(url_for("auth.login"))

        flash(message, "danger")

    return render_template("signup.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form["email"]
        password = request.form["password"]

        user = AuthService.login_user(
            email,
            password
        )

        if user:

            login_user(user)

            flash(
                "Login Successful!",
                "success"
            )

            return redirect(
                url_for("dashboard")
            )

        flash(
            "Invalid Email or Password",
            "danger"
        )

    return render_template("login.html")


@auth_bp.route("/logout")
def logout():

    logout_user()

    flash(
        "Logged Out Successfully.",
        "success"
    )

    return redirect(
        url_for("auth.login")
    )