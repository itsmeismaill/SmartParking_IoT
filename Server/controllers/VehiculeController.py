
from flask import jsonify, request
from models.Vehicule import Vehicule
from models.Abonnement import Abonnement
from flask import Blueprint
import cv2
from PIL import Image
from pytesseract import pytesseract
# import serial



vehicule = Blueprint('vehicule', __name__)

camera = cv2.VideoCapture(0)


# arduino_serial = serial.Serial('COM4', 9600, timeout=1)

# Shared camera resource


# def turn_on_led(color):
#     if color == 'red':
#         arduino_serial.write(b'R')
#     elif color == 'green':
#         arduino_serial.write(b'G')


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


# Check by matricule a travers string matricule
@vehicule.route('/vehicules/checkabonnement/<string:matricule>', methods=['GET'], )
def check_matricule_abonnement(matricule):
    vehicule = Vehicule.get_by_matricule(Vehicule("",matricule,"",""))
    if not vehicule:
        # turn_on_led('red')
        return "vehicule not found",401
    
    #GET ABONNEMENT
    if(vehicule['abonnement_id'] is None):
        # turn_on_led('red')
        return "vehicule has no abonnement yet",402

    abonnement=Abonnement.get_by_id(Abonnement(vehicule['abonnement_id'],'',''))

    if(abonnement['duree']>0):
        # turn_on_led('green')
        return "Bariel open",200

    # turn_on_led('red')
    return "Abonnement expired",403


# Check by matricule a travers camera
@vehicule.route('/vehicules/checkabonnementrealtime/', methods=['GET'], )
def check_matricule_abonnement_realtime():

    # Lire matricule a travers camera
    matricule = capture_and_recognize()
    
    print("string is : "+matricule)

    vehicule = Vehicule.get_by_matricule(Vehicule("",matricule,"",""))
    if not vehicule:
        return "vehicule not found",401
    
        
    #GET ABONNEMENT
    if(vehicule['abonnement_id'] is None):
        return "vehicule has no abonnement yet",402
        
    abonnement=Abonnement.get_by_id(Abonnement(vehicule['abonnement_id'],'',''))

    if(abonnement['duree'] > 0):
        return "Bariel open",200
        
    return "Abonnement expired",403
    

# Fonction pour appliquer la reconnaissance et retourne le texte
def capture_and_recognize():

    text=""

    # tentatives
    tentative1=""
    tentative2=""

    while True:
        _, image = camera.read()
        cv2.imshow('Text detection', image)

        # Appliquer la reconnaissance de texte
        path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        pytesseract.tesseract_cmd = path_to_tesseract
        text = pytesseract.image_to_string(Image.fromarray(image))

        print("Texte détecté : ", text[:-1]) 

        if text[:-1]:
            tentative1=str(text[:-1]).replace("\n", "").replace(" ","")
            if tentative1==tentative2:
                # matriculeFormat = tentative1.split("|");

                ## EXAMPLE OF THE MATRICULE "1234|A|1"
                # if len(matriculeFormat) == 3 and tentative1.count("|") == 2 and tentative1.index("|") == 4 and tentative1.rindex("|") == 6:
                # print("correct Format : " + matriculeFormat[1])
                return tentative1
            else:
                tentative2=tentative1
                tentative1=""


# TODO when link the rasp with arduino: Turn on the LED (Green) if the conditions of a car has satisfied totally otherwise LED (Red),

# TODO: Calculate the Difference time between In and Out of the car

# TODO: Check If the subscription of User finished or never
