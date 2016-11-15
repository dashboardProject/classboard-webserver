from flask import Blueprint

dashboardServer = Blueprint('dashboardServer', __name__, template_folder='../templates', static_folder='../static')