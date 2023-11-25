import datetime
import time
from flask import Flask, render_template, Response
from models.Vehicule import Vehicule
from models.TimeParking import TimeParking
from models.Abonnement import Abonnement
from connection_db import conn
import pytesseract
from flask_cors import CORS
from flask_session import Session
import secrets
from controllers.UserController import user
from controllers.AbonnementController import abonnement
from controllers.VehiculeController import vehicule
from PIL import Image

# from flask_socketio import SocketIO
import cv2
import base64
from threading import Thread

from common import app, socketio

# app = Flask(__name__)

CORS(app)

app.register_blueprint(user)
app.register_blueprint(abonnement)
app.register_blueprint(vehicule)

# socketio = SocketIO(app, cors_allowed_origins="*")

camera = cv2.VideoCapture(0)


def webcam():
    camera = cv2.VideoCapture(0)
    text = ""

    # Tentatives
    tentative1 = ""
    tentative2 = ""

    while True:
        success, frame = camera.read()
        if success:
            ret, buffer = cv2.imencode('.jpg', frame)

            # Appliquer la reconnaissance de texte
            path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            pytesseract.tesseract_cmd = path_to_tesseract
            text = pytesseract.image_to_string(Image.fromarray(frame))

            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

            print("Texte détecté : ", text[:-1])
            if text[:-1]:
                tentative1 = str(text[:-1]).replace("\n", "").replace(" ", "")
                if tentative1 == tentative2:
                   matricule=tentative1
                   vehicule = Vehicule.get_by_matricule(Vehicule("",matricule,"",""))
                   if not vehicule:
                        print("------------------------------------")
                        print("#       vehicule not found         #")
                        print("------------------------------------")
                        time.sleep(10)
                   else:
                        abonnement=Abonnement.get_by_id(vehicule['abonnement_id'])
                        timeparking = TimeParking.get_last_by_date_entrer(TimeParking("",vehicule["id"],None,None))
                       
                        if(len(timeparking)>0 and timeparking[0]['date_sortie'] is None):
                            
                            #calcul difference between two date time
                            duration_seconds = int(((datetime.datetime.now()) - timeparking[0]['date_entree']).total_seconds())
                 
                            #new duration
                            new_duration = duration_seconds//60
                            
                            print(abonnement["duree"]-new_duration)

                            # update abonnement object
                            Abonnement.update(Abonnement(abonnement["id"],abonnement["duree"]-new_duration,abonnement["montant"]))

                            timeparkingData = {
                                'vehicule_id': "timeparking['vehicule_id']",
                                'date_entree': "timeparking['date_entree']",
                                'date_sortie': "datetime.datetime.now()"
                            }

                            # update time prking object object
                            TimeParking.update(TimeParking(timeparking[0]["id"],timeparking[0]["vehicule_id"],timeparking[0]["date_entree"],datetime.datetime.now()))

                            socketio.emit('car_event', {'message': 'Car exit successfully', 'timeparking': timeparkingData})
                            print("------------------------------------")
                            print("#      Car go out of parking       #")
                            print("------------------------------------")
                            time.sleep(10)

                        else:
                            #GET ABONNEMENT
                            if(vehicule['abonnement_id'] is None):
                                # turn_on_led('red')
                                    print("------------------------------------")
                                    print("#  vehicule has no abonnement yet  #")
                                    print("------------------------------------")
                                    time.sleep(10)
                            else:
                                abonnement=Abonnement.get_by_id(vehicule['abonnement_id'])
                                if(abonnement['duree']>0):
                                    timeparking = TimeParking("",vehicule["id"],datetime.datetime.now(),None)
                                    timeparking.save()

                                    timeparkingData = {
                                        'vehicule_id': "timeparking['vehicule_id']",
                                        'date_entree': "timeparking['date_entree']",
                                    }
                                    socketio.emit('car_event', {'message': 'Car entered successfully', 'timeparking': timeparkingData})

                                    print("------------------------------------")
                                    print("#      Car entred successfuly      #")
                                    print("------------------------------------")
                                    time.sleep(10)
                                else:
                                    print("------------------------------------")
                                    print("#        Abonnement expired        #")
                                    print("------------------------------------")
                                    time.sleep(10)
                else:
                    tentative2 = tentative1
                    tentative1 = ""
        else:
            break  # Exit the loop if capturing fails

    camera.release()

@app.route('/webcam')
def webcam_display():
    return Response(webcam(), mimetype='multipart/x-mixed-replace; boundary=frame')

@socketio.on('connect')
def handle_connect():
    print('Client connected')
    socketio.emit('connected', 'Connected to server')

@socketio.on('disconnect')
def handle_disconnect():
    print('Client disconnected')

if __name__ == '__main__':
    print("secret key", app.config['SECRET_KEY'])
    app.run(port=5000, debug=True)


# !!
# from flask import Flask, render_template, Response
# from flask_cors import CORS
# from flask_socketio import SocketIO
# import cv2
# import base64
# from threading import Thread

# app = Flask(__name__)
# CORS(app)
# socketio = SocketIO(app, cors_allowed_origins="*")

# camera = cv2.VideoCapture(0)

# def webcam():
#     camera = cv2.VideoCapture(0)

#     while True:
#         success, frame = camera.read()
#         if success:
    
#             ret, buffer = cv2.imencode('.jpg', frame)
#             frame = buffer.tobytes()
#             yield (b'--frame\r\n'
#                    b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
#         else:
#             camera.release()

# @app.route('/webcam')
# def webcam_display():
#     return Response(webcam(), mimetype='multipart/x-mixed-replace; boundary=frame')

# @socketio.on('connect')
# def handle_connect():
#     print('Client connected')
#     socketio.emit('connected', 'Connected to server')

# @socketio.on('disconnect')
# def handle_disconnect():
#     print('Client disconnected')

# if __name__ == '__main__':
#     socketio.run(app, port=5000, debug=True)



