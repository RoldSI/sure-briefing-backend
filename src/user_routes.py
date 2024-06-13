from flask import Blueprint

user_bp = Blueprint('user', __name__, url_prefix='/user')

# @user_bp.route('/status')
# def user_status():
#     return "status"

@user_bp.route('/subscribe')
def user_subscribe():
    return "subscribe"

@user_bp.route('/unsubscribe')
def user_unsubscribe():
    return "unsubscribe"

@user_bp.route('/delivery')
def user_delivery():
    return "delivery"
