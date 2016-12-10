import webapp2

from database_Model import User
from utils.decorators import userCheck
from utils.userNgroupQuery import selectUser
from google.appengine.api import users
from configs import JINJA_ENV, SIGNUP_PAGE, MANAGEMENT_PAGE

class SignIn(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()

        if user:
            userMail = user.email()

            if selectUser(userMail).count() is 0:
                self.response.write(JINJA_ENV.get_template(SIGNUP_PAGE).render())

            else:
                self.redirect_to('management')

            return

        self.redirect(users.create_login_url(self.request.uri))

class SignUp(webapp2.RequestHandler):
    def get(self):
        user = users.get_current_user()
        userMail = user.email()

        if selectUser(userMail).count() is 0:
            User(userMail = userMail).put()

        self.redirect_to('management')

class ManageUserData(webapp2.RequestHandler):
    @userCheck
    def post(self):
        self.response.write('sadf')