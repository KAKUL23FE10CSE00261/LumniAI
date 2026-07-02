from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_required, current_user

from app.services.profile_service import ProfileService

profile_bp = Blueprint("profile", __name__)


@profile_bp.route("/profile", methods=["GET", "POST"])
@login_required
def profile():

    if request.method == "POST":

        success, message = ProfileService.save_profile(
            current_user.id,
            request.form
        )

        flash(message, "success" if success else "danger")

        return redirect(url_for("profile.profile"))

    profile = ProfileService.get_profile(current_user.id)

    return render_template(
        "profile.html",
        profile=profile
    )