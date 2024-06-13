import os
import firebase_admin
from firebase_admin import credentials, auth
from flask import request, jsonify
from functools import wraps

# Initialize Firebase Admin SDK
SERVICE_ACCOUNT_KEY_PATH = "local/sure-briefing-firebase-adminsdk-gujpp-4bfdd17f96.json"
if os.path.exists(SERVICE_ACCOUNT_KEY_PATH):
    # If the service account key JSON file is present
    cred = credentials.Certificate(SERVICE_ACCOUNT_KEY_PATH)
    firebase_admin.initialize_app(cred)
else:
    # If the service account key JSON file is not present, use default credentials
    firebase_admin.initialize_app()

def authenticated(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'Authorization' not in request.headers:
            return jsonify({"message": "Token is missing!"}), 401
        
        token = request.headers['Authorization'].split(" ")[1]
        try:
            decoded_token = auth.verify_id_token(token)
            request.user = decoded_token
        except Exception as e:
            return jsonify({"message": "Token is invalid!", "error": str(e)}), 401
        
        return f(*args, **kwargs)
    
    return decorated