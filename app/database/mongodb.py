from app.extensions import mongo


def get_db():
    return mongo.db