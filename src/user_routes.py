from flask import Blueprint, jsonify

user_bp = Blueprint('user', __name__, url_prefix='/user')

@user_bp.route('/status')
def user_status():
    return "status"

@user_bp.route('/subscribe', methods=['POST'])
def user_subscribe():
    return jsonify({"message": "subscribe"}), 200

@user_bp.route('/unsubscribe', methods=['POST'])
def user_unsubscribe():
    return jsonify({"message": "unsubscribe"}), 200

@user_bp.route('/delivery', methods=['POST'])
def user_delivery():
    return jsonify({"message": "delivery"}), 200
