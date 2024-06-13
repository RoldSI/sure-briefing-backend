from flask import Blueprint, jsonify, request

from src.authentication import authenticated

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/status', methods=['GET'])
@authenticated
def user_status():
    user_id = request.user['uid']
    response = {"message": f"Status for user with ID: {user_id}"}
    return jsonify(response), 200

@user_bp.route('/subscribe', methods=['POST'])
@authenticated
def user_subscribe():
    user_id = request.user['uid']
    response = {"message": f"Subscribed user with ID: {user_id}"}
    return jsonify(response), 200

@user_bp.route('/unsubscribe', methods=['POST'])
@authenticated
def user_unsubscribe():
    user_id = request.user['uid']
    response = {"message": f"Unsubscribed user with ID: {user_id}"}
    return jsonify(response), 200

@user_bp.route('/delivery', methods=['POST'])
@authenticated
def user_delivery():
    user_id = request.user['uid']
    response = {"message": f"Delivery for user with ID: {user_id}"}
    return jsonify(response), 200
