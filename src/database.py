import os
from pymongo import MongoClient

user = os.getenv('MONGO_USER')
password = os.getenv('MONGO_PASSWORD')
host = os.getenv('MONGO_HOST')
db_name = os.getenv('MONGO_DB')

if not all([user, password, host, db_name]):
    raise ValueError("One or more MongoDB environment variables are not set")

client = MongoClient(f"mongodb+srv://{user}:{password}@{host}/?retryWrites=true&w=majority&appName=SURE-Briefing")
db = client[db_name]
user_collection = db['user']

def check_and_create_user(user_id):
    user = user_collection.find_one({"user_id": user_id})
    
    if user is None:
        default_user = {
            "user_id": user_id,
            "stripe_id": None,
            "subscribed": True,
            "deliver": {"email": None},
            "region": "europe"
        }
        user_collection.insert_one(default_user)
        return default_user
    return user

def set_delivery_email(user_id, email):
    result = user_collection.update_one(
        {"user_id": user_id},
        {"$set": {"deliver.email": email}}
    )
    return result.modified_count > 0

def set_subscription_status(user_id, status):
    result = user_collection.update_one(
        {"user_id": user_id},
        {"$set": {"subscribed": status}}
    )
    return result.modified_count > 0

def subscribe_user(user_id):
    return set_subscription_status(user_id, True)

def unsubscribe_user(user_id):
    return set_subscription_status(user_id, False)
