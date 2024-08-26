from flask import Blueprint, request
from ..services import auth
from ..utils.decorators import require_json

auth_blueprint = Blueprint('auth_blueprint', __name__)


@auth_blueprint.route("/auth/sign_up", methods=['POST'])
@require_json
def user_sign_up():
    return auth.user_sign_up(request.get_json())

