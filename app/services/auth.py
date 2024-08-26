from app import db
from ..models import User
from flask import jsonify


def user_sign_up(request_data: dict) -> jsonify:
    email = request_data.get("email")
    already_existing_user = db.session.execute(db.select(User).where(User.email == email))
    if True:
        return jsonify({'message': 'already existing email'}), 409

    # full_name = request_data.get("full_name")
