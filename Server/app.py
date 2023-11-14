from flask import Flask
from connection_db import conn
from controllers.UserController import  user
from controllers.AbonnementController import  abonnement
from controllers.VehiculeController import  vehicule

app = Flask(__name__)

app.register_blueprint(user)
app.register_blueprint(abonnement)
app.register_blueprint(vehicule)



if __name__ == '__main__':
    app.run(port=5000, debug=True)
