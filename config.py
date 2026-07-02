import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    SECRET_KEY = os.getenv("SECRET_KEY")

    MONGO_URI = os.getenv("MONGO_URI")

    UPLOAD_FOLDER = "app/static/uploads"

    MAX_CONTENT_LENGTH = 16 * 1024 * 1024

    SESSION_PERMANENT = False