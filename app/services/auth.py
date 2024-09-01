# TODO create the create_auth_token function

from app import db
from ..models import User
from flask import jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from ..utils.functions import create_http_response
from ..utils.validations import UserInputsValidation
from dotenv import load_dotenv
import os
from flask_jwt_extended import create_access_token
from cryptography.fernet import Fernet
from datetime import timedelta

load_dotenv()

encryption_key = os.getenv("FERNET_KEY")
fernet = Fernet(encryption_key)


def user_sign_up(request_data: dict) -> jsonify:
    email = request_data.get("email")
    full_name = request_data.get("full_name")
    unhashed_password = request_data.get("password")

    UserInputsValidation.validate_existence(email, full_name, unhashed_password)
    UserInputsValidation.email_validation(email)
    UserInputsValidation.password_validation(unhashed_password)

    already_existing_user = db.session.execute(db.select(User).where(User.email == email)).scalar()
    if already_existing_user:
        return create_http_response('already existing email', 'failed', 409)

    new_user = User(
        full_name=full_name,
        password=generate_password_hash(unhashed_password, method='pbkdf2:sha256', salt_length=8),
        email=email
    )

    db.session.add(new_user)
    db.session.commit()

    return create_http_response(
        message='Successfully registered',
        status='success',
        http_status=201,
        auth_token=create_auth_token(new_user)
    )


def login(request_data: dict) -> jsonify:
    email = request_data.get("email")
    password = request_data.get("password")
    UserInputsValidation.validate_existence(email, password)
    UserInputsValidation.email_validation(email)

    user = db.session.execute(db.select(User).where(User.email == email)).scalar()
    if not user:
        return create_http_response('Invalid email or password', 'failed', 400)

    if not check_password_hash(user.password, password):
        return create_http_response('Invalid email or password', 'failed', 400)
    else:
        return create_http_response(
            message='Login successful',
            status='success',
            http_status=200,
            auth_token=create_auth_token(user)
        )


def create_auth_token(user: User) -> str:
    identity = user.full_name
    additional_claims = {'id': user.id}
    access_token = create_access_token(
        identity,
        additional_claims=additional_claims,
        expires_delta=timedelta(hours=24)
    )

    return fernet.encrypt(access_token.encode()).decode()


