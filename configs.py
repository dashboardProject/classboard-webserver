import os
import jinja2

JINJA_ENV = jinja2.Environment(loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')),
                               extensions=['jinja2.ext.autoescape'],
                               autoescape=True)

MAIN_PAGE = '/main.html'
SIGNUP_PAGE = '/signup.html'
USERINFO_PAGE = '/user_infomation.html'
MAKE_GROUP = '/management_makegroup.html'
MANAGEMENT_PAGE = '/management_main.html'
MANAGEMENT_GROUP = '/management_group.html'
MANAGEMENT_DEVICE = '/management_device.html'
MANAGEMENT_CONTENTS = '/management_contents.html'
TUTORIAL_PAGE = '/tutorial.html'

DEVICE_INIT = '/d_init.html'
DEVICE_MAIN = '/d_main.html'