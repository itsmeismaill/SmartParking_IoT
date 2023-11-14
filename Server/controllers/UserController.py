from models.User import User
from flask import jsonify, request
from flask import Blueprint

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
    user = User(data['id'],data['username'],data['cin'],data['telephone'],data['password'],data['email'],data['role'])
    user.save()
    return jsonify(user.__dict__)


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



#  deja_tester = true


