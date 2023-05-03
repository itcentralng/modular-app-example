from flask import Blueprint, request

from app.user.database import User

user = Blueprint('user', __name__, url_prefix='/user')

@user.post('/login')
def login():
    email = request.json.get('email')
    password = request.json.get('password')
    if email and password:
        user = User.get_by_email(email)
        if user and user.is_valid(password):
            return 'Login succcessful'
    return 'User not found', 401

@user.post('/register')
def register():
    email = request.json.get('email')
    password = request.json.get('password')
    if email and password:
        user = User.create(email, password)
        return 'Registration succcessful', 200
    return 'Email and Password Required', 400