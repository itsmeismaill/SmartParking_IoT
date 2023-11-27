import datetime
import cv2
from PIL import Image
from pytesseract import pytesseract
from flask import jsonify, request
from models.Vehicule import Vehicule
from models.Abonnement import Abonnement
from models.TimeParking import TimeParking
from flask import Blueprint

from flask_socketio import emit
from common import socketio

from models.User import User

# import serial

vehicule = Blueprint('vehicule', __name__)

# camera = cv2.VideoCapture(0)


# arduino_serial = serial.Serial('COM4', 9600, timeout=1)

# Shared camera resource


# def turn_on_led(color):
#     if color == 'red':
#         arduino_serial.write(b'R')
#     elif color == 'green':
#         arduino_serial.write(b'G')


@vehicule.route('/vehicules', methods=['GET'])
def get_all_vehicules():
    vehicules = Vehicule.get_all()

    vehicules_with_abonnement = []
    for vehicule in vehicules:
        if isinstance(vehicule, dict):
            abonnement_id = vehicule.get('abonnement_id')
        else:
            abonnement_id = vehicule.abonnement_id

        abonnement = Abonnement.get_by_id(abonnement_id)

        userId = vehicule.get('user_id') if isinstance(vehicule, dict) else vehicule.user_id;

        userData = User.get_by_id(User (userId,"","","","","",""))
        print("userData, ", userData)


        vehicule_data = {
            'id': vehicule.get('id') if isinstance(vehicule, dict) else vehicule.id,
            'matricule': vehicule.get('matricule') if isinstance(vehicule, dict) else vehicule.matricule,
            'abonnement_id': abonnement_id,
            'user_id': userId,
            'username': userData.get("username"),
            'duree_abonnement': abonnement.get('duree') if abonnement else None
        }
        vehicules_with_abonnement.append(vehicule_data)

    return jsonify(vehicules_with_abonnement)


@vehicule.route('/vehiculesUsers', methods=['GET'])
def get_all_vehicules_users():
    vehicules = Vehicule.get_all()
    print("vehicules, ", vehicules);
    return jsonify(vehicules)

@vehicule.route('/vehicules/<int:id>', methods=['GET'], )
def get_vehicule_by_id(id):
    vehicule = Vehicule.get_by_id(Vehicule (id,"","",""))

    print(vehicule)


    # socketio.emit('car_entered', {'message': 'Car entered successfully', 'timeparking': vehicule})
    return jsonify(vehicule)



@vehicule.route('/vehicules_users/<int:userId>', methods=['GET'])
def get_vehicules_users_by_id(userId):
    
    if userId:
        vehicules = Vehicule.get_all_by_user(userId)
        # Get subscription information for each vehicle
        vehicule_info = []
        for vehicule in vehicules:
            abonnement = Abonnement.get_by_id(vehicule.get('abonnement_id'))
            print("======"+abonnement)
            times_parking = TimeParking.get_by_vehicule_id(TimeParking("",vehicule["id"],None,None))
            for time_parking in times_parking:
                print(time_parking)
                duration_seconds = int((time_parking['date_sortie']-time_parking['date_entree']).total_seconds())
                hours, remainder = divmod(duration_seconds, 3600)
                minutes, seconds = divmod(remainder, 60)
                # Format the result
                time_parking['difference'] = "{:02}h{:02}m{:02}s".format(hours, minutes, seconds)

            print(times_parking)
            # hours, remainder = divmod(abonnement["duree"].seconds, 3600)
            # minutes, seconds = divmod(remainder, 60)
            # abonnement["duree"]="{:02}h{:02}m{:02}s".format(hours, minutes, seconds)
            vehicule_info.append({'vehicule': vehicule, 'abonnement': abonnement ,'time_parking':times_parking})
            print(vehicule_info)
        return jsonify(vehicule_info)
    else:
        return jsonify({'error': 'User not authenticated'}), 401


@vehicule.route('/vehicules', methods=['POST'], )
def add_vehicule():
    data = request.get_json()
    vehicule = Vehicule(0, data['matricule'], data['abonnementId'], data['userId'])
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


@vehicule.route('/vehicules/matricule/<string:matricule>', methods=['GET'],)
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
        # turn_on_led('red')
        return "vehicule not found",401
    
    #GET ABONNEMENT
    if(vehicule['abonnement_id'] is None):
        # turn_on_led('red')
        return "vehicule has no abonnement yet",402

    abonnement=Abonnement.get_by_id(vehicule['abonnement_id'])
    if(abonnement['duree']>0):
        timeparking = TimeParking("",vehicule["id"],datetime.datetime.now(),None)
        timeparking.save()



        socketio.emit('car_entered', {'message': 'Car entered successfully', 'timeparking': timeparking})

        return "Car entred successfuly",202

    # turn_on_led('red')
    return "Abonnement expired",403

# car go out test matricule string
@vehicule.route('/vehicules/car_exit/<string:matricule>', methods=['GET'], )
def car_exit(matricule):
    vehicule = Vehicule.get_by_matricule(Vehicule("",matricule,"",""))
    if not vehicule:
        return "vehicule not found",401
    abonnement=Abonnement.get_by_id(vehicule['abonnement_id'])
    timeparking = TimeParking.get_last_by_date_entrer(TimeParking("",vehicule["id"],None,None))[0]

    #calcul difference between two date time
    
    duration_seconds = int(((datetime.datetime.now())-timeparking["date_entree"]).total_seconds())
    # Convert duration to a time format (HH:MM:SS)
    # formatted_duration = str(datetime.timedelta(seconds=duration_seconds))
    print(type(duration_seconds))
    print(duration_seconds)
    #new duration
    new_duration = duration_seconds//60
    print(abonnement["duree"]-new_duration)
    # update abonnement object
    Abonnement.update(Abonnement(abonnement["id"],abonnement["duree"]-new_duration,abonnement["montant"]))

    # update time prking object object
    TimeParking.update(TimeParking(timeparking["id"],timeparking["vehicule_id"],timeparking["date_entree"],datetime.datetime.now()))

    timeparkingData = {
        'id': timeparking['id'],
        'vehicule_id': timeparking['vehicule_id'],
        'date_entree': timeparking['date_entree'],
        'date_sortie': str(datetime.datetime.now())
    }

    socketio.emit('car_entered', {'message': 'Car entered successfully', 'timeparking': timeparkingData})


    return "Car go out of parking",200


# car even in or out matricule string
@vehicule.route('/vehicules/car_in_out/<string:matricule>', methods=['GET'], )
def car_in_out(matricule):
    vehicule = Vehicule.get_by_matricule(Vehicule("",matricule,"",""))
    if not vehicule:
        return "vehicule not found",401
    abonnement=Abonnement.get_by_id(vehicule['abonnement_id'])
    timeparking = TimeParking.get_last_by_date_entrer(TimeParking("",vehicule["id"],None,None))[0]

    user = User.get_by_id(vehicule['user_id'])

    if(timeparking['date_sortie'] is None):
        #calcul difference between two date time
        duration_seconds = int(((datetime.datetime.now())-timeparking["date_entree"]).total_seconds())
        # Convert duration to a time format (HH:MM:SS)
        # formatted_duration = str(datetime.timedelta(seconds=duration_seconds))
        print(type(duration_seconds))
        print(duration_seconds)
        #new duration
        new_duration = duration_seconds//60
        print(abonnement["duree"]-new_duration)
        # update abonnement object
        Abonnement.update(Abonnement(abonnement["id"],abonnement["duree"]-new_duration,abonnement["montant"]))


        # update time prking object object
        TimeParking.update(TimeParking(timeparking["id"],timeparking["vehicule_id"],timeparking["date_entree"],datetime.datetime.now()))

        timeparkingData = {
            'matricule': matricule,
            'clientName': user.username,
            'date_entree': timeparking["date_entree"],
            'date_sortie': datetime.datetime.now()
        }

        socketio.emit('car_event', {'message': 'Car exit successfully', 'timeparking': timeparkingData})

        
        return "Car go out of parking",200
    else:
        #GET ABONNEMENT
        if(vehicule['abonnement_id'] is None):
            # turn_on_led('red')
            return "vehicule has no abonnement yet",402

        abonnement=Abonnement.get_by_id(vehicule['abonnement_id'])
        if(abonnement['duree']>0):
            timeparking = TimeParking("",vehicule["id"],datetime.datetime.now(),None)
            timeparking.save()

            timeparkingData = {
                'matricule': matricule,
                'clientName': user.username,
                'date_entree': datetime.datetime.now(),
                'date_sortie': "stationnée"
            }
            socketio.emit('car_event', {'message': 'Car entered successfully', 'timeparking': timeparkingData})

            return "Car entred successfuly",202

        # turn_on_led('red')
        return "Abonnement expired",403

    

# # car enter a travers camera
# @vehicule.route('/vehicules/car_entred_realtime/', methods=['GET'], )
# def car_entred_realtime():

#     #Lire matricule a travers camera
#     matricule = capture_and_recognize()
    
#     print("string is : "+matricule)

#     vehicule = Vehicule.get_by_matricule(Vehicule("",matricule,"",""))
#     if not vehicule:
#         return "vehicule not found",401
    
        
#     #GET ABONNEMENT
#     if(vehicule['abonnement_id'] is None):
#         return "vehicule has no abonnement yet",402

#     return "Abonnement expired",403
    
# # car go out a travers camera
# @vehicule.route('/vehicules/car_go_out_realtime/', methods=['GET'], )
# def car_go_out_realtime():

#     #Lire matricule a travers camera
#     matricule = capture_and_recognize()
    
#     print("string is : "+matricule)
    
#     vehicule = Vehicule.get_by_matricule(Vehicule("",matricule,"",""))
#     if not vehicule:
#         return "vehicule not found",401
#     abonnement=Abonnement.get_by_id(vehicule['abonnement_id'])
#     timeparking = TimeParking.get_last_by_date_entrer(TimeParking("",vehicule["id"],None,None))[0]

#     #calcul difference between two date time
    
#     duration_seconds = int(((datetime.datetime.now())-timeparking["date_entree"]).total_seconds())

#     # Convert duration to a time format (HH:MM:SS)
#     # formatted_duration = str(datetime.timedelta(seconds=duration_seconds))
    
#     #new duration
#     new_duration = datetime.timedelta(seconds=abonnement["duree"].total_seconds()-duration_seconds)

#     # update abonnement object
#     Abonnement.update(Abonnement(abonnement["id"],new_duration,abonnement["montant"]))

#     # update time prking object object
#     TimeParking.update(TimeParking(timeparking["id"],timeparking["vehicule_id"],timeparking["date_entree"],datetime.datetime.now()))

#     socketio.emit('car_entered', {'message': 'Car entered successfully', 'timeparking': timeparkingData})

#     return "Car go out of parking",200



# #Fonction pour appliquer la reconnaissance et retourne le texte
# def capture_and_recognize():

#     text=""

#     #tentatives
#     tentative1=""
#     tentative2=""

#     while True:
#         _, image = camera.read()
#         cv2.imshow('Text detection', image)

#         #Appliquer la reconnaissance de texte
#         path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
#         pytesseract.tesseract_cmd = path_to_tesseract
#         text = pytesseract.image_to_string(Image.fromarray(image))

#         print("Texte détecté : ", text[:-1]) 
#         if text[:-1]:
#             tentative1=str(text[:-1]).replace("\n", "").replace(" ","")
#             if tentative1==tentative2:
#                 # matriculeFormat = tentative1.split("|");

#                 ## EXAMPLE OF THE MATRICULE "1234|A|1"
#                 # if len(matriculeFormat) == 3 and tentative1.count("|") == 2 and tentative1.index("|") == 4 and tentative1.rindex("|") == 6:
#                 # print("correct Format : " + matriculeFormat[1])
#                 return tentative1
#             else:
#                 tentative2=tentative1
#                 tentative1=""


# TODO when link the rasp with arduino: Turn on the LED (Green) if the conditions of a car has satisfied totally otherwise LED (Red),

# TODO: Calculate the Difference time between In and Out of the car

# TODO: Check If the subscription of User finished or never
