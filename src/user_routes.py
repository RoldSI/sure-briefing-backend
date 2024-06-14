from flask import Blueprint, jsonify, request

from src.authentication import authenticated
from src.database import check_and_create_user, subscribe_user, unsubscribe_user, set_delivery_email

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/status', methods=['GET'])
@authenticated
def user_status():
    user_id = request.user['uid']
    check_and_create_user(user_id)
    response = {"message": f"Status for user with ID: {user_id}"}
    return jsonify(response), 200

@user_bp.route('/subscribe', methods=['POST'])
@authenticated
def user_subscribe():
    user_id = request.user['uid']
    check_and_create_user(user_id)
    subscribe_user(user_id)
    response = {"message": f"Subscribed user with ID: {user_id}"}
    return jsonify(response), 200

@user_bp.route('/unsubscribe', methods=['POST'])
@authenticated
def user_unsubscribe():
    user_id = request.user['uid']
    check_and_create_user(user_id)
    unsubscribe_user(user_id)
    response = {"message": f"Unsubscribed user with ID: {user_id}"}
    return jsonify(response), 200

@user_bp.route('/delivery', methods=['POST'])
@authenticated
def user_delivery():
    user_id = request.user['uid']
    check_and_create_user(user_id)
    email = request.json.get('email')
    set_delivery_email(user_id, email)
    response = {"message": f"Delivery for user with ID: {user_id}"}
    return jsonify(response), 200
