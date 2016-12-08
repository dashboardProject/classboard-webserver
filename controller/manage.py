import json
import webapp2

from database_Model import User, GroupMap
from utils.decorators import userCheck
from utils.userNgroupQuery import selectUser, selectGroupsOfUser, selectGroup
from google.appengine.api import users
from configs import JINJA_ENV, TUTORIAL_PAGE, MANAGEMENT_PAGE,MANAGEMENT_CONTENTS,\
                      MANAGEMENT_GROUP, MANAGEMENT_DEVICE, DEVICE_MAIN


class Tutorial(webapp2.RequestHandler):
    # access mainpage
    def get(self):
        # add query and template data
        self.response.write(JINJA_ENV.get_template(TUTORIAL_PAGE).render())


class Management(webapp2.RequestHandler):
    # access mainpage
    # @userCheck
    def get(self):
        user = users.get_current_user()

        userMail = user.email()
        userId = selectUser(userMail).get().key.id()
        groupIdList = selectGroupsOfUser(userId).get().groupId()
        groupNameList = selectGroup(None, groupIdList).get().groupName()

        # add query and template data
        self.response.write(JINJA_ENV.get_template(MANAGEMENT_PAGE).render())


class ManagementGroup(webapp2.RequestHandler):
    # access mainpage
    @userCheck
    def get(self):
        # add query and template data
        self.response.write(JINJA_ENV.get_template(MANAGEMENT_GROUP).render())


class ManagementDevice(webapp2.RequestHandler):
    # access mainpage
    @userCheck
    def get(self):
        # add query and template data
        self.response.write(JINJA_ENV.get_template(MANAGEMENT_DEVICE).render())


class ManagementContents(webapp2.RequestHandler):
    # access mainpage
    @userCheck
    def get(self):
        # add query and template data
        self.response.write(JINJA_ENV.get_template(MANAGEMENT_CONTENTS).render())


class DeviceMain(webapp2.RequestHandler):
    # access mainpage
    @userCheck
    def get(self, dkey):
        # add query and template data
        self.response.write(JINJA_ENV.get_template(DEVICE_MAIN).render())


class DeviceMethod(webapp2.RequestHandler):
    # access mainpage
    def get(self, dkey, method):
        self.response.headers['Content-Type'] = 'application/json'
        obj = {
            'dkey': dkey,
            'dname': '446',
            'start': '8:00',
            'end': '20:00'
        }
        self.response.out.write(json.dumps(obj))