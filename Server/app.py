from flask import Flask
from connection_db import conn
from controllers.UserController import  user
from controllers.AbonnementController import  abonnement
from controllers.VehiculeController import  vehicule
from controllers.AuthController import auth

app = Flask(__name__)

app.register_blueprint(user)
app.register_blueprint(abonnement)
app.register_blueprint(vehicule)
app.register_blueprint(auth)



if __name__ == '__main__':
    app.run(port=5000, debug=True)
