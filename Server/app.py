from flask import Flask, render_template, Response
from connection_db import conn

from flask_cors import CORS
from flask_session import Session
import secrets
from controllers.UserController import user
from controllers.AbonnementController import abonnement
from controllers.VehiculeController import vehicule

from flask_socketio import SocketIO
import cv2
import base64
from threading import Thread


app = Flask(__name__)
app.config['SECRET_KEY'] = secrets.token_hex(16)  # Générez une clé secrète unique
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_COOKIE_SECURE'] = True
app.config.from_object(__name__)
Session(app)  # Assurez-vous d'utiliser la même instance de Session ici

CORS(app, supports_credentials=True)
app.register_blueprint(user)
app.register_blueprint(abonnement)
app.register_blueprint(vehicule)

socketio = SocketIO(app, cors_allowed_origins="*")

camera = cv2.VideoCapture(0)

def webcam():
    camera = cv2.VideoCapture(0)

    while True:
        success, frame = camera.read()
        if success:
    
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        else:
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



