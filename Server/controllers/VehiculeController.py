
from flask import jsonify, request
from models.Vehicule import Vehicule
from flask import Blueprint

vehicule = Blueprint('vehicule', __name__)

@vehicule.route('/vehicules', methods=['GET'], )
def get_all_vehicules():
    vehicules = Vehicule.get_all()
    return jsonify(vehicules)

@vehicule.route('/vehicules/<int:id>', methods=['GET'], )
def get_vehicule_by_id(id):
    vehicule = Vehicule.get_by_id(id)
    return jsonify(vehicule)

@vehicule.route('/vehicules', methods=['POST'], )
def add_vehicule():
    data = request.get_json()
    vehicule = Vehicule(data['id'],data['matricule'],data['abonnement_id'],data['user_id'])
    vehicule.save()
    return jsonify(vehicule.__dict__)


@vehicule.route('/vehicules/<int:id>', methods=['PUT'], )
def update_vehicule(id):
    data = request.get_json()
    vehicule = Vehicule(data['id'],data['matricule'],data['abonnement_id'],data['user_id'])
    vehicule.update()
    return jsonify(vehicule)

@vehicule.route('/vehicules/<int:id>', methods=['DELETE'], )
def delete_vehicule(id):
    vehicule = Vehicule(id,"","","")
    vehicule.delete()
    return jsonify(vehicule)

@vehicule.route('/vehicules/matricule/<string:matricule>', methods=['GET'], )
def get_vehicule_by_matricule(matricule):
    vehicule = Vehicule.get_by_matricule(matricule)
    return jsonify(vehicule)

@vehicule.route('/vehicules/user/<int:user_id>', methods=['GET'], )
def get_vehicule_by_user_id(user_id):
    vehicule = Vehicule.get_by_user_id(user_id)
    return jsonify(vehicule)

@vehicule.route('/vehicules/abonnement/<int:abonnement_id>', methods=['GET'], )
def get_vehicule_by_abonnement_id(abonnement_id):
    vehicule = Vehicule.get_by_abonnement_id(abonnement_id)
    return jsonify(vehicule)

