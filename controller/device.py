import json
import time
import webapp2

import logging
from database_Model import Group, GroupMap
from utils.decorators import userCheck
from utils.userNgroupQuery import selectUser, selectGroupsOfUser, selectGroup, selectUsersInGroup, selectMap
from utils.deviceQuery import selectDeviceWithGroup
from utils.contentQuery import selectContentWithGroup
from google.appengine.api import users, mail
from configs import JINJA_ENV, DEVICE_MAIN


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