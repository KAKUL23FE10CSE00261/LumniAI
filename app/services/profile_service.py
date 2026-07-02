from bson import ObjectId

from app.database.collections import profiles_collection


class ProfileService:

    @staticmethod
    def save_profile(user_id, form):

        profile = {

            "user_id": ObjectId(user_id),

            # Personal Information
            "full_name": form["full_name"],
            "age": int(form["age"]),
            "gender": form["gender"],
            "height": float(form["height"]),
            "weight": float(form["weight"]),

            # Lifestyle
            "water_intake": float(form["water_intake"]),
            "sleep_hours": float(form["sleep_hours"]),
            "exercise": form["exercise"],
            "stress_level": form["stress_level"],
            "smoking": form["smoking"],
            "alcohol": form["alcohol"],

            # Skin Information
            "skin_type": form["skin_type"],
            "skin_tone": form["skin_tone"],
            "sensitive_skin": form["sensitive_skin"],
            "acne_history": form["acne_history"],
            "pigmentation": form["pigmentation"],
            "allergies": form["allergies"],

            # Medical
            "medical_conditions": form["medical_conditions"],
            "medications": form["medications"]

        }

        profiles_collection.update_one(
            {"user_id": ObjectId(user_id)},
            {"$set": profile},
            upsert=True
        )

        return True, "Profile saved successfully."

    @staticmethod
    def get_profile(user_id):

        return profiles_collection.find_one(
            {"user_id": ObjectId(user_id)}
        )