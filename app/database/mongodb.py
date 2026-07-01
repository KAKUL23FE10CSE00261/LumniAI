from app import mongo


def get_db():
    """
    Returns the MongoDB database instance.
    """
    return mongo.db