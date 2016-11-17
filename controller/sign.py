import webapp2
from configs import JINJA_ENV, SIGNIN_PAGE, SIGNUP_PAGE

class Sign_In(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENV.get_template(SIGNIN_PAGE).render())

class Sign_Up(webapp2.RequestHandler):
    def get(self):
        self.response.write(JINJA_ENV.get_template(SIGNUP_PAGE).render())