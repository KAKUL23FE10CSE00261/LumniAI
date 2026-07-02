from flask_login import UserMixin
from bson.objectid import ObjectId

from app.database.collections import users_collection


class User(UserMixin):

    def __init__(self, user_data):
        self.id = str(user_data["_id"])
        self.name = user_data["name"]
        self.email = user_data["email"]
        self.username = user_data["username"]
        self.user_data = user_data

    @staticmethod
    def get_by_email(email):
        user = users_collection.find_one({"email": email})

        if user:
            return User(user)

        return None

    @staticmethod
    def get_by_id(user_id):

        try:
            user = users_collection.find_one(
                {"_id": ObjectId(user_id)}
            )

            if user:
                return User(user)

        except Exception:
            pass

        return None