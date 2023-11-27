from flask import jsonify, request , Blueprint
from models.TimeParking import TimeParking
from models.Vehicule import Vehicule
from models.User import User
from models.Abonnement import Abonnement

timeparking = Blueprint('timeparking', __name__)

@timeparking.route('/timeparkings', methods=['GET'], )
def get_all_timeparkings():
    timeparkings = TimeParking.get_all()

    timeparkings_with_vehicule = []

    for timeparking in timeparkings:

        vehicule_id = timeparking['vehicule_id']

        vehicule = Vehicule.get_by_id( Vehicule(vehicule_id, "", "", ""))

        user = User.get_by_id(User(vehicule['user_id'], "", "", "", "", "", ""))

        abonnement = Abonnement.get_by_id(vehicule['abonnement_id'])

        timeparking_with_vehicule = {
            'id': timeparking['id'],
            'vehicule_id': timeparking['vehicule_id'],
            'date_entree': str(timeparking['date_entree']),
            'date_sortie': str(timeparking['date_sortie']),
            'matricule': vehicule['matricule'],
            'duree': abonnement['duree'],
            'clientName': user['username'],
        }

        print('-----------------', timeparking_with_vehicule, '-----------------')

        timeparkings_with_vehicule.append(timeparking_with_vehicule)

    return jsonify(timeparkings_with_vehicule)

@timeparking.route('/timeparkings/<int:id>', methods=['GET'], )
def get_timeparking_by_id(id):
    timeparking = TimeParking.get_by_id(TimeParking (id,"","",""))
    return jsonify(timeparking)

@timeparking.route('/timeparkings', methods=['POST'], )
def add_timeparking():
    data = request.get_json()
    timeparking = TimeParking(data['id'],data['vehicule_id'],data['date_entree'],data['date_sortie'])
    timeparking.save()
    return jsonify(timeparking.__dict__)

@timeparking.route('/timeparkings/<int:id>', methods=['PUT'], )
def update_timeparking(id):
    data = request.get_json()
    timeparking = TimeParking(data['id'],data['vehicule_id'],data['date_entree'],data['date_sortie'])
    timeparking.update()
    return jsonify(timeparking.__dict__)

@timeparking.route('/timeparkings/<int:id>', methods=['DELETE'], )
def delete_timeparking(id):
    timeparking = TimeParking(id,"","","")
    timeparking.delete()
    return jsonify(timeparking.__dict__)

@timeparking.route('/timeparkings/vehicule/<int:vehicule_id>', methods=['GET'], )
def get_timeparking_by_vehicule_id(vehicule_id):
    timeparking = TimeParking.get_by_vehicule_id(vehicule_id)
    return jsonify(timeparking)


