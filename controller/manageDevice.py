import webapp2

from database_Model import User
from utils.decorators import userCheck
from utils.userNgroupQuery import selectUser
from google.appengine.api import users
from configs import JINJA_ENV, SIGNUP_PAGE, MAIN_PAGE

class Register_Device(webapp2.RequestHandler):
    def post(self):
        self.response.write(JINJA_ENV.get_template().render())

class Mapping_Content(webapp2.RequestHandler):
    def post(self):
        self.response.write(JINJA_ENV.get_template().render())

class Modify_DeviceInfo(webapp2.RequestHandler):
    def post(self):
        self.response.write(JINJA_ENV.get_template().render())