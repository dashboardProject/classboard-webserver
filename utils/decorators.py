import webapp2
from google.appengine.api import users
from utils.userNgroupQuery import selectUser
from configs import *

def userCheck(func):
    def decorated_function(*args, **kwargs):
        user = users.get_current_user()

        if user:
            if len(selectUser(user.user_id())) is 1:
                return func(*args, **kwargs)

            else:
                return webapp2.redirect(SIGNUP_PAGE)

        else:
            return webapp2.redirect(SIGNIN_PAGE)

    return decorated_function