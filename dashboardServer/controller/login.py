from flask import request, url_for, render_template
from dashboardServer.dashboard_blueprint import dashboardServer
from google.appengine.api import users


def checkLoginState():
    return

@dashboardServer.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        error = checkLoginState(request.form)

    isLogin = True

    if isLogin:
        return render_template('main.html')

    else:
        return 'asdf'