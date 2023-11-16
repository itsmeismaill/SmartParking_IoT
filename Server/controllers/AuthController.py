from flask import Blueprint, jsonify, request, session, redirect, url_for
from models.User import User

auth = Blueprint('auth', __name__)

@auth.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    new_user = User(
        id=None,
        username=data['username'],
        cin=data['cin'],
        telephone=data['telephone'],
        password=data['password'],
        email=data['email'],
        role=data['role']
    )
    
    if new_user.save():
        return jsonify({'message': 'Registration successful'})
    else:
        return jsonify({'message': 'Registration failed'})

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    if User.check_password(username, password):
        session['username'] = username
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Login failed'})


@auth.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return jsonify({'message': 'Logout successful'})
