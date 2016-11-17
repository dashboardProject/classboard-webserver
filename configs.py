import os
import jinja2

JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
                               extensions=['jinja2.ext.autoescape'],
                               autoescape=True)

MAIN_PAGE = '/main.html'
SIGNIN_PAGE = '/main.html'#''/signin'
SIGNUP_PAGE = '/main.html'#'signup'