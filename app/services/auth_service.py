from app.database.collections import users_collection
from app.models.user import User
from app.utils.password import hash_password, verify_password


class AuthService:

    @staticmethod
    def register_user(form):

        # Check Email
        if users_collection.find_one({"email": form["email"]}):
            return False, "Email already registered."

        # Check Username
        if users_collection.find_one({"username": form["username"]}):
            return False, "Username already exists."

        # Password Match
        if form["password"] != form["confirm_password"]:
            return False, "Passwords do not match."

        user = {

            "name": form["name"],

            "email": form["email"],

            "username": form["username"],

            "age": int(form["age"]),

            "gender": form["gender"],

            "password": hash_password(form["password"])

        }

        users_collection.insert_one(user)

        return True, "Registration Successful."

    @staticmethod
    def login_user(email, password):

        user = User.get_by_email(email)

        if user is None:
            return None

        if verify_password(
                user.user_data["password"],
                password):

            return user

        return None