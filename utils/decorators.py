import webapp2
import logging
from configs import *
from functools import wraps
from google.appengine.api import users
from utils.userNgroupQuery import selectUser

def userCheck(func):

    @wraps(func)
    def decorated_function(self, *args):
        user = users.get_current_user()

        # check google account
        if user:
            # check app account
            if selectUser(user.user_id()).count is 1:
                return func(self, *args)

            else:
                return webapp2.redirect_to('signup')

        # not sign-in google account yet
        else:
            return webapp2.redirect(users.create_login_url(self.request.uri))

    return decorated_function