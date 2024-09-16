from dotenv import load_dotenv
load_dotenv()
import os

from flask import make_response, request
from werkzeug.security import check_password_hash, generate_password_hash
import jwt
from . import app, db
from .models import Funds, Users
from datetime import datetime, timedelta


@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    email = data.get("email")
    firstName = data.get("firstName")
    lastName = data.get("lastName")
    password = data.get("password")

    if firstName and lastName and email and password:
        user = Users.query.filter_by(email=email).first()
        if user:
            return make_response({"message": "Please Sign In"}, 409)

        user = (
            Users(
                email=email,
                password=generate_password_hash(password),
                firstName=firstName,
                lastName=lastName,
            ),
        )

        db.session.add(user)
        db.session.commit()

        return make_response({"message": "User created"}, 201)

    return make_response({"message": "Unable to create user"}, 500)

@app.route("/login", methods=["POST"])
def login():
    auth = request.json
    if not auth or not auth.get('email') or not auth.get('password'):
        return make_response({"message": "Missing credentials"}, 401)

    user = Users.query.filter_by(email = auth.get('email')).first()
    if not user:
        return make_response({"message": "User not found"}, 401)

    if check_password_hash(user.password, auth.get('password')):
        token = jwt.encode(
            {"id": user.id, "exp": datetime.utcnow() + timedelta(minutes=30)},
            os.getenv("JWT_ACCESS_SECRET"),
            os.getenv("JWT_ACCESS_HASH"),
        )
        return make_response({"access_tiken": token}, 200)

    return make_response({"message": 'Invalid credential'}, 401)
