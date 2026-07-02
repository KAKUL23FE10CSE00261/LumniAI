import os
import uuid

from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    session,
    url_for,
    current_app,
    flash
)

from werkzeug.utils import secure_filename

from app.services.skin_issue_predictor import predict_skin_issue

upload_bp = Blueprint(
    "upload",
    __name__
)

ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@upload_bp.route("/upload", methods=["GET", "POST"])
def upload():

    if request.method == "GET":
        return render_template("upload.html")

    if "image" not in request.files:
        flash("Please upload an image.")
        return redirect(request.url)

    file = request.files["image"]

    if file.filename == "":
        flash("Please select an image.")
        return redirect(request.url)

    if not allowed_file(file.filename):
        flash("Only JPG, JPEG and PNG images are allowed.")
        return redirect(request.url)

    filename = secure_filename(file.filename)

    extension = filename.rsplit(".", 1)[1].lower()

    unique_filename = f"{uuid.uuid4()}.{extension}"

    upload_folder = os.path.join(
        current_app.root_path,
        "static",
        "uploads"
    )

    os.makedirs(upload_folder, exist_ok=True)

    image_path = os.path.join(
        upload_folder,
        unique_filename
    )

    file.save(image_path)

    result = predict_skin_issue(image_path)

    session["skin_issue"] = result["skin_issue"]

    session["confidence"] = result["confidence"]

    session["uploaded_image"] = unique_filename

    return redirect(
        url_for("questionnaire.questionnaire")
    )