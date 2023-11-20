import datetime
import cv2
from PIL import Image
from pytesseract import pytesseract
from flask import jsonify, request, session
from models.Vehicule import Vehicule
from models.Abonnement import Abonnement
from models.TimeParking import TimeParking
from flask import Blueprint

vehicule = Blueprint('vehicule', __name__)


# Shared camera resource
camera = cv2.VideoCapture(0)


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
    user_id = session.get("user_id")
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


# car enter test matricule string
@vehicule.route('/vehicules/car_entred/<string:matricule>', methods=['GET'], )
def car_entred(matricule):
    vehicule = Vehicule.get_by_matricule(Vehicule("",matricule,"",""))
    if not vehicule:
        return "vehicule not found",401
    
    #GET ABONNEMENT
    if(vehicule['abonnement_id'] is None):
        return "vehicule has no abonnement yet",402

    abonnement=Abonnement.get_by_id(vehicule['abonnement_id'])
    if(abonnement['duree']!=datetime.timedelta(hours=0, minutes=0)):
        timeparking = TimeParking("",vehicule["id"],datetime.datetime.now(),None)
        timeparking.save()
        return "Car entred successfuly",202

    return "Abonnement expired",403

# car go out test matricule string
@vehicule.route('/vehicules/car_go_out/<string:matricule>', methods=['GET'], )
def car_go_out(matricule):
    vehicule = Vehicule.get_by_matricule(Vehicule("",matricule,"",""))
    if not vehicule:
        return "vehicule not found",401
    abonnement=Abonnement.get_by_id(vehicule['abonnement_id'])
    timeparking = TimeParking.get_last_by_date_entrer(TimeParking("",vehicule["id"],None,None))[0]

    #calcul difference between two date time
    
    duration_seconds = int(((datetime.datetime.now())-timeparking["date_entree"]).total_seconds())

    # Convert duration to a time format (HH:MM:SS)
    # formatted_duration = str(datetime.timedelta(seconds=duration_seconds))
    
    #new duration
    new_duration = datetime.timedelta(seconds=abonnement["duree"].total_seconds()-duration_seconds)

    # update abonnement object
    Abonnement.update(Abonnement(abonnement["id"],new_duration,abonnement["montant"]))

    # update time prking object object
    TimeParking.update(TimeParking(timeparking["id"],timeparking["vehicule_id"],timeparking["date_entree"],datetime.datetime.now()))


    return "Car go out of parking",200



# car enter a travers camera
@vehicule.route('/vehicules/car_entred_realtime/', methods=['GET'], )
def car_entred_realtime():

    #Lire matricule a travers camera
    matricule = capture_and_recognize()
    
    print("string is : "+matricule)
    
    vehicule = Vehicule.get_by_matricule(Vehicule("",matricule,"",""))
    if not vehicule:
        return "vehicule not found",401
    
    #GET ABONNEMENT
    if(vehicule['abonnement_id'] is None):
        return "vehicule has no abonnement yet",402

    abonnement=Abonnement.get_by_id(vehicule['abonnement_id'])
    if(abonnement['duree']!=datetime.timedelta(hours=0, minutes=0)):
        timeparking = TimeParking("",vehicule["id"],datetime.datetime.now(),None)
        timeparking.save()
        return "Car entred successfuly",202

    return "Abonnement expired",403
    
# car go out a travers camera
@vehicule.route('/vehicules/car_go_out_realtime/', methods=['GET'], )
def car_go_out_realtime():

    #Lire matricule a travers camera
    matricule = capture_and_recognize()
    
    print("string is : "+matricule)
    
    vehicule = Vehicule.get_by_matricule(Vehicule("",matricule,"",""))
    if not vehicule:
        return "vehicule not found",401
    abonnement=Abonnement.get_by_id(vehicule['abonnement_id'])
    timeparking = TimeParking.get_last_by_date_entrer(TimeParking("",vehicule["id"],None,None))[0]

    #calcul difference between two date time
    
    duration_seconds = int(((datetime.datetime.now())-timeparking["date_entree"]).total_seconds())

    # Convert duration to a time format (HH:MM:SS)
    # formatted_duration = str(datetime.timedelta(seconds=duration_seconds))
    
    #new duration
    new_duration = datetime.timedelta(seconds=abonnement["duree"].total_seconds()-duration_seconds)

    # update abonnement object
    Abonnement.update(Abonnement(abonnement["id"],new_duration,abonnement["montant"]))

    # update time prking object object
    TimeParking.update(TimeParking(timeparking["id"],timeparking["vehicule_id"],timeparking["date_entree"],datetime.datetime.now()))


    return "Car go out of parking",200



#Fonction pour appliquer la reconnaissance et retourne le texte
def capture_and_recognize():

    text=""

    #tentatives
    tentative1=""
    tentative2=""

    while True:
        _, image = camera.read()
        cv2.imshow('Text detection', image)

        #Appliquer la reconnaissance de texte
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(Image.fromarray(image))

        print("Texte détecté : ", text[:-1]) 
        if text[:-1]:
            tentative1=str(text[:-1]).replace("\n", "").replace(" ","")
            if tentative1==tentative2:
                return tentative1
            else:
                tentative2=tentative1
                tentative1=""

