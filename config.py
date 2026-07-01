import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()


class Config:
    # Flask Secret Key
    SECRET_KEY = os.getenv("SECRET_KEY")

    # MongoDB Connection String
    MONGO_URI = os.getenv("MONGO_URI")

    # Session Configuration
    SESSION_PERMANENT = False

    # Upload Folder (for future image uploads)
    UPLOAD_FOLDER = "app/static/uploads"

    # Maximum Upload Size (10 MB)
    MAX_CONTENT_LENGTH = 10 * 1024 * 1024