from app.database.mongodb import get_db

db = get_db()

users_collection = db["users"]
profiles_collection = db["profiles"]
analysis_collection = db["analysis"]
recommendations_collection = db["recommendations"]
history_collection = db["history"]
reports_collection = db["reports"]
chatbot_logs_collection = db["chatbot_logs"]