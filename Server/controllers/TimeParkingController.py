from flask import jsonify, request , Blueprint
from models.TimeParking import TimeParking

timeparking = Blueprint('timeparking', __name__)

@timeparking.route('/timeparkings', methods=['GET'], )
def get_all_timeparkings():
    timeparkings = TimeParking.get_all()
    return jsonify(timeparkings)

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

