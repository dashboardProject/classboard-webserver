import webapp2
from configs import JINJA_ENV, SIGNUP_PAGE
from utils.decorators import userCheck

class Sign_Up(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENV.get_template(SIGNUP_PAGE).render())

@userCheck
class Manage_User_Data(webapp2.RequestHandler):
    def post(self):
        self.response.write('sadf')

class test(webapp2.RequestHandler):
    def get(self):
        self.response.write('sadf')