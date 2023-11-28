from flask import jsonify, request , Blueprint
from models.TimeParking import TimeParking
from models.Vehicule import Vehicule
from models.User import User
from models.Abonnement import Abonnement

timeparking = Blueprint('timeparking', __name__)

@timeparking.route('/timeparkings', methods=['GET'], )
def get_all_timeparkings():
    vehicules = Vehicule.get_all()
    print("--------------vehicules-----------------",vehicules)

    timeparkings_with_vehicule = []
    

    for vehicule in vehicules:
        print("---------------------------------", vehicule["id"])
        
        timeparking = TimeParking.get_last_by_date_entrer(TimeParking("", vehicule["id"],None,None))
        
        user = User.get_by_id(User(vehicule['user_id'], "", "", "", "", "", ""))

        abonnement = Abonnement.get_by_id(vehicule['abonnement_id'])
        #  print("--------------matricule-----------------",vehicule['matricule'])
        #  print('---------------id time parking-----------',timeparking['id'])
        #  print('---------------v-id-----------',timeparking['vehicule_id'])



        timeparking_with_vehicule = {
            'id': timeparking[0]['id'] if timeparking and len(timeparking) > 0 else None,
            'vehicule_id': timeparking[0]['vehicule_id'] if timeparking and len(timeparking) > 0 else None,
            'date_entree': str(timeparking[0]['date_entree']) if timeparking and len(timeparking) > 0 else None,
            'date_sortie': str(timeparking[0]['date_sortie']) if timeparking and len(timeparking) > 0 else None,
            'matricule': vehicule['matricule'],
            'duree': abonnement['duree'],
            'clientName': user['username'],
         }


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


