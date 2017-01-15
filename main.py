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
import webapp2, logging

from google.appengine.api import users
from utils.decorators import userCheck
from configs import JINJA_ENV, MAIN_PAGE, USERINFO_PAGE
from utils.userNgroupQuery import selectUser
from controller.sign import SignIn, SignUp, ManageUserData
from controller.manage import Tutorial, Management, ManagementDevice, ManagementGroup,\
                                 MakeGroup, InvitationUser, SecessionUser, GroupRename, AddDevice, ModifiedDevice, DeleteDevice  #, ManagementContents
from controller.device import DeviceMain, DeviceMethod

class Main(webapp2.RequestHandler):
    # access mainpage
    def get(self):
        user = users.get_current_user()
        userNickname = ''

        if user and selectUser(user.email()).count() is 1:
            userNickname = selectUser(user.email()).get().nickname

        template_values = {'userNickname': userNickname, }
        self.response.write(JINJA_ENV.get_template(MAIN_PAGE).render(template_values))

class UserInfo(webapp2.RequestHandler):
    @userCheck
    def get(self):
        user = users.get_current_user()
        userNickname = selectUser(user.email()).get().nickname
        template_values = {'userMail': user.email(),
                           'userNickname': userNickname, }

        self.response.write(JINJA_ENV.get_template(USERINFO_PAGE).render(template_values))
        
app = webapp2.WSGIApplication([webapp2.Route('/', Main, name='main'),
                               webapp2.Route('/signin', SignIn, name='signin'),
                               webapp2.Route('/signup', SignUp, name='signup'),
                               webapp2.Route('/userinfo', UserInfo, name='userinfo'),
                               webapp2.Route('/updateuserinfo', ManageUserData),
                               webapp2.Route('/tutorial', Tutorial),
                               webapp2.Route('/management', Management, name='management'),
                               webapp2.Route('/management/makegroup', MakeGroup),
                               webapp2.Route('/management/<:(\d*)>/group', ManagementGroup, name='managegroup'),
                               webapp2.Route('/management/<:(\d*)>/group/invite', InvitationUser, name='invite'),
                               webapp2.Route('/management/<:(\d*)>/group/rename', GroupRename, name='rename'),
                               webapp2.Route('/management/<:(\d*)>/group/secession', SecessionUser, name='secession'),
                               webapp2.Route('/management/<:(\d*)>/device', ManagementDevice),
                               webapp2.Route('/management/<:(\d*)>/device/registration', AddDevice),
                               webapp2.Route('/management/<:(\d*)>/device/modify', ModifiedDevice),
                               webapp2.Route('/management/<:(\d*)>/device/del<:(\d*)>', DeleteDevice),
#                                webapp2.Route('/management/contents', ManagementContents),
                               webapp2.Route(r'/d/<dkey:\S{12}><:/?>', DeviceMain),
                               webapp2.Route(r'/d/<dkey:\S{12}>/<method:(info|mod)><:/?>', DeviceMethod),
                               ],debug=True)