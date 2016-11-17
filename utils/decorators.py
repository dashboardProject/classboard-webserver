import webapp2
from google.appengine.api import users
from utils.userNgroupQuery import selectUser
from configs import *

def userCheck(func):
    def decorated_function(*args, **kwargs):
        user = users.get_current_user()

        # check google account
        if user:
            # check app account
            if selectUser(user.user_id()).count is 1:
                return func(*args, **kwargs)

            else:
                return webapp2.redirect(SIGNUP_PAGE)

        # not sign-in google account yet
        else:
            return webapp2.redirect(users.create_login_url(webapp2.RequestHandler.request.uri))

    return decorated_function