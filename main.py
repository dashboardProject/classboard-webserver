#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2

from database_Model import User
from google.appengine.api import users
from configs import JINJA_ENV, MAIN_PAGE
from utils.userNgroupQuery import selectUser
from controller.sign import Sign_Up, Manage_User_Data, test


class Main(webapp2.RequestHandler):
    # access mainpage
    def get(self):
        user = users.get_current_user()

        if user and selectUser(user.user_id()).count is 1:
            # add query and template data

            self.response.write(JINJA_ENV.get_template(MAIN_PAGE).render())

        else:
            self.response.write(JINJA_ENV.get_template(MAIN_PAGE).render())

    # sign-in request
    def post(self):
        user = users.get_current_user()

        if user and selectUser(user.user_id()).count is 0:
            self.response.write(JINJA_ENV.get_template(Sign_Up).render())

        else:
            self.redirect(users.create_login_url(self.request.uri))

app = webapp2.WSGIApplication([('/', Main),
                               ('/signup', Sign_Up),
                               ('/updateuserinfo', Manage_User_Data),
                               ('/test', test)],
                              debug=True)
