import webapp2
from configs import JINJA_ENV

class test(webapp2.RequestHandler):
    def get(self):
        self.response.write('welcome!!!!!!!')
        # self.response.write(JINJA_ENV.get_template('main.html').render())