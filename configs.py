import os
import jinja2

JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
                               extensions=['jinja2.ext.autoescape'],
                               autoescape=True)

MAIN_PAGE = '/'
SIGNIN_PAGE = '/'#''/signin'
SIGNUP_PAGE = '/'#'signup'