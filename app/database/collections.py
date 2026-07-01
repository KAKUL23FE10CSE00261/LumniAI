from app.database.mongodb import get_db

db = get_db()

# Collections
users_collection = db["users"]
profiles_collection = db["profiles"]
analysis_collection = db["analysis_history"]
recommendations_collection = db["recommendations"]
chat_history_collection = db["chat_history"]
reports_collection = db["reports"]