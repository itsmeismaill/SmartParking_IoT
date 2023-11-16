from flask import Flask
from connection_db import conn
from controllers.UserController import  user
from controllers.AbonnementController import  abonnement
from controllers.VehiculeController import  vehicule
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.register_blueprint(user)
app.register_blueprint(abonnement)
app.register_blueprint(vehicule)



if __name__ == '__main__':
    app.run(port=5000, debug=True)
