from models.User import User
from flask import jsonify, request
from flask import Blueprint,session
import bcrypt

user = Blueprint('user', __name__)

@user.route('/users', methods=['GET'], )
def get_all_users():
    users = User.get_all()
    return jsonify(users)

@user.route('/users/<int:id>', methods=['GET'], )
def get_user_by_id(id):
    user = User.get_by_id(User (id,"","","","","",""))
    return jsonify(user)

@user.route('/users', methods=['POST'], )
def add_user():
    data = request.get_json()
    print(data)
    data['password'] = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
    user = User(data['id'],data['username'],data['cin'],data['telephone'], data['password'] ,data['email'],data['role'])
    
    user.save()
    return jsonify(user)


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

    if User.check_password(username, password):
        return jsonify({'message': 'Login successful'})
    else:
        return jsonify({'message': 'Login failed'})


@user.route('/logout', methods=['GET'])
def logout():
    session.clear()
    return jsonify({'message': 'Logout successful'})


#  deja_tester = true


