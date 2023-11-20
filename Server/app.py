from flask import Flask
from flask_cors import CORS
from flask_session import Session
import secrets
from controllers.UserController import user
from controllers.AbonnementController import abonnement
from controllers.VehiculeController import vehicule

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

if __name__ == '__main__':
    print("secret key", app.config['SECRET_KEY'])
    app.run(port=5000, debug=True)
