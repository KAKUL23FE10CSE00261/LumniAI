from app.database.user_collection import users_collection
from app.utils.password import hash_password, verify_password


class AuthService:

    @staticmethod
    def register_user(data):

        if users_collection.find_one({"email": data["email"]}):
            return False, "Email already exists"

        user = {
            "name": data["name"],
            "email": data["email"],
            "username": data["username"],
            "age": int(data["age"]),
            "gender": data["gender"],
            "password": hash_password(data["password"])
        }

        users_collection.insert_one(user)

        return True, "Registration Successful"

    @staticmethod
    def login_user(email, password):

        user = users_collection.find_one({"email": email})

        if not user:
            return None

        if verify_password(user["password"], password):
            return user

        return None