import os
import uuid
from werkzeug.utils import secure_filename
from flask import current_app


class ImageService:

    ALLOWED_EXTENSIONS = {"png", "jpg", "jpeg"}

    @staticmethod
    def allowed_file(filename):

        return (
            "." in filename and
            filename.rsplit(".", 1)[1].lower()
            in ImageService.ALLOWED_EXTENSIONS
        )

    @staticmethod
    def save_image(image, user_id):

        if image is None or image.filename == "":
            return False, "Please select an image.", None

        if not ImageService.allowed_file(image.filename):
            return False, "Only JPG, JPEG and PNG images are allowed.", None

        filename = secure_filename(image.filename)

        extension = filename.rsplit(".", 1)[1].lower()

        unique_filename = f"{uuid.uuid4()}.{extension}"

        upload_folder = os.path.join(
            current_app.config["UPLOAD_FOLDER"],
            str(user_id)
        )

        os.makedirs(upload_folder, exist_ok=True)

        image_path = os.path.join(
            upload_folder,
            unique_filename
        )

        image.save(image_path)

        return (
            True,
            "Image uploaded successfully.",
            unique_filename
        )