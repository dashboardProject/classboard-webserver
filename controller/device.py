import json
import time
import webapp2

import logging
from database_Model import Group, GroupMap, Device
from utils.decorators import userCheck
import utils.deviceQuery
from google.appengine.api import users, mail
from configs import JINJA_ENV, DEVICE_MAIN, DEVICE_INIT


def deviceAdd(hashKey):
    Device(deviceKey=hashKey).put()


class DeviceMain(webapp2.RequestHandler):
    # access mainpage
    def get(self, dkey):
        try:
            device = utils.deviceQuery.selectDeviceWithHashkey(dkey)
        except :
            deviceAdd(dkey)
            self.response.write(JINJA_ENV.get_template(DEVICE_INIT).render({'key':dkey}))
        
        # add query and template data
        self.response.write(JINJA_ENV.get_template(DEVICE_MAIN).render({'key':dkey,'name':Device.deviceName,'gCal':Device.googleCalendarId}))


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
        