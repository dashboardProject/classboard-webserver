from controller import *
from flask import Flask
from dashboard_blueprint import dashboardServer

def create_app(debug=False, testing=False, config_overrides=None):
    app = Flask(__name__)

    app.secret_key = 'asdJIL3109ASKL'

    app.debug = debug
    app.testing = testing

    app.register_blueprint(dashboardServer)

    return app