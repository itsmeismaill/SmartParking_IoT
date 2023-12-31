
from models.User import User
from flask import jsonify, request
from flask import Blueprint,session
# import bcrypt

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

user = Blueprint('user', __name__)


@user.route('/users', methods=['GET'], )
def get_all_users():
    users = User.get_all()
    return users

@user.route('/users/<int:id>', methods=['GET'], )
def get_user_by_id(id):
    user = User.get_by_id(User (id,"","","","","",""))
    return jsonify(user)

@user.route('/users', methods=['POST'])
def add_user():
    try:
        data = request.get_json()

        required_fields = ['username', 'cin', 'telephone', 'password', 'email']
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required field: {field}")

        hashed_password = bcrypt.generate_password_hash(data['password']).decode('utf-8')

        user = User(
            id=0,
            username=data['username'],
            cin=data['cin'],
            telephone=data['telephone'],
            password=hashed_password,
            email=data['email'],
            role="client"
        )

        user.save()

        return jsonify({'message': 'User created successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 400


@user.route('/users/<int:id>', methods=['PUT'], )
def update_user(id):
    data = request.get_json()
    user = User(id,data['username'],data['cin'],data['telephone'],data['password'],data['email'],data['role'])
    user.update()
    return jsonify(user.__dict__)

@user.route('/users/<int:id>', methods=['DELETE'], )
def delete_user(id):
    user = User(id,"","","","","","")
    user.delete()
    return jsonify(user.__dict__)

@user.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    username = data['username']
    password = data['password']

    user = User.get_by_username(username)

    print(f"Stored hashed password: {user.password}")
    print(f"Entered password: {password}")

    if user and bcrypt.check_password_hash(user.password, password):
        user_data = {
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'role': user.role,
        }

        return jsonify({
            'message': 'Login successful',
            'user': user_data
        })
    
    # if User.check_password(username, password):
    #     MyUser = User.get_by_username(username)
    #     print("MyUser_Id", MyUser.id)
    #     session['user_id'] = MyUser.id
    #     print("session---------------------------", session)
    #     return jsonify({'message': 'Login successful'})
    
    else:
        return jsonify({'message': 'Login failed'})
    

@user.route('/logout', methods=['POST'])
def logout():
    # session.clear()
    return jsonify({'message': 'Logout successful'})


#  deja_tester = true


