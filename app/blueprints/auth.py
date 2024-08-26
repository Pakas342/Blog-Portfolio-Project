from flask import Blueprint, request

authentication_blueprint = Blueprint('authentication_blueprint', __name__)


@authentication_blueprint.route("/auth/sign_up", methods=['POST'])
def user_signup():
    pass
