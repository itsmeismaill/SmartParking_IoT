
from flask import jsonify, request
from models.Abonnement import Abonnement
from flask import Blueprint

abonnement = Blueprint('abonnement', __name__)

@abonnement.route('/abonnements', methods=['GET'], )
def get_all_abonnements():
    abonnements = Abonnement.get_all()
    return jsonify(abonnements)

@abonnement.route('/abonnements/<int:id>', methods=['GET'], )
def get_abonnement_by_id(id):
    abonnement = Abonnement.get_by_id(Abonnement (id,"",""))
    return jsonify(abonnement)

@abonnement.route('/abonnements', methods=['POST'], )
def add_abonnement():
    data = request.get_json()
    abonnement = Abonnement(0,data['duree']*60,data['montant'])
    savedAbd = abonnement.save()
    print(savedAbd)
    return jsonify(savedAbd.__dict__)


@abonnement.route('/abonnements/<int:id>', methods=['PUT'], )
def update_abonnement(id):
    data = request.get_json()
    abonnement = Abonnement(data['id'],data['duree'],data['montant'])
    abonnement.update()
    return jsonify(abonnement.__dict__)

@abonnement.route('/abonnements/<int:id>', methods=['DELETE'], )
def delete_abonnement(id):
    abonnement = Abonnement(id,"","")
    abonnement.delete()
    return jsonify(abonnement.__dict__)


