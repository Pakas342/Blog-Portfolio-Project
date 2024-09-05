from flask import Blueprint, request
from ..services import auth
from ..utils.decorators import require_json

auth_blueprint = Blueprint('auth_blueprint', __name__)


@auth_blueprint.route("/auth/signup", methods=['POST'])
@require_json(methods=['POST'])
def user_sign_up():
    return auth.user_sign_up(request.get_json())


@auth_blueprint.route("/auth/login", methods=['POST'])
@require_json(methods=['POST'])
def user_log_in():
    return auth.login(request.get_json())

