
from flask import jsonify, request , session
from flask_jwt_extended import get_jwt_identity , jwt_required
from models.Vehicule import Vehicule
from flask import Blueprint
from models.Abonnement import Abonnement
from controllers.UserController import user


vehicule = Blueprint('vehicule', __name__)

@vehicule.route('/vehicules', methods=['GET'])
def get_all_vehicules():
    vehicules = Vehicule.get_all()

    # Récupérer la durée de chaque abonnement associé à chaque véhicule
    vehicules_with_abonnement = []
    for vehicule in vehicules:
        if isinstance(vehicule, dict):
            abonnement_id = vehicule.get('abonnement_id')
        else:
            abonnement_id = vehicule.abonnement_id

        # Utiliser la méthode Abonnement.get_by_id pour récupérer l'abonnement
        abonnement = Abonnement.get_by_id(abonnement_id)

        vehicule_data = {
            'id': vehicule.get('id') if isinstance(vehicule, dict) else vehicule.id,
            'matricule': vehicule.get('matricule') if isinstance(vehicule, dict) else vehicule.matricule,
            'abonnement_id': abonnement_id,
            'user_id': vehicule.get('user_id') if isinstance(vehicule, dict) else vehicule.user_id,
            'duree_abonnement': abonnement.get('duree') if abonnement else None
        }
        vehicules_with_abonnement.append(vehicule_data)

    return jsonify(vehicules_with_abonnement)

@vehicule.route('/vehicules/<int:id>', methods=['GET'], )
def get_vehicule_by_id(id):
    vehicule = Vehicule.get_by_id(Vehicule (id,"","",""))
    return jsonify(vehicule)

@vehicule.route('/vehicules_users', methods=['GET'])
def get_vehicules_users_by_id():
  

    user_id=11
    print("mon id", user_id)
    
    if user_id:
        vehicules = Vehicule.get_all_by_user(user_id)
        print(vehicules)
        
        # Get subscription information for each vehicle
        vehicule_info = []
        for vehicule in vehicules:
            abonnement = Abonnement.get_by_id(vehicule.get('abonnement_id'))
            vehicule_info.append({'vehicule': vehicule, 'abonnement': abonnement})

        return jsonify(vehicule_info)
    else:
        return jsonify({'error': 'User not authenticated'}), 401


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

