import webapp2

from database_Model import User
from utils.decorators import userCheck
from utils.userNgroupQuery import selectUser
from google.appengine.api import users
from configs import JINJA_ENV, SIGNUP_PAGE, MAIN_PAGE

class Sign_Up(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        userMail = user.email()
        if selectUser(userMail).count is 0:
            User(userMail).put()

        self.response.write(JINJA_ENV.get_template(MAIN_PAGE).render())

class Manage_User_Data(webapp2.RequestHandler):
    @userCheck
    def post(self):
        self.response.write('sadf')

class test(webapp2.RequestHandler):
    @userCheck
    def get(self):
        user = users.get_current_user()
        self.response.write(user.email())