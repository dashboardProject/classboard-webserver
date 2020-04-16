# -*- coding: utf-8 -*-

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
        
        device = utils.deviceQuery.selectDeviceWithHashkey(dkey).get()
        #a='''        
        if device == None :
            deviceAdd(dkey)
            self.response.write(JINJA_ENV.get_template(DEVICE_INIT).render({'dkey':dkey,'key':dkey[:4]+' - '+dkey[4:8]+' - '+dkey[8:]}))            
        elif device.registeredGroupId == None:
            self.response.write(JINJA_ENV.get_template(DEVICE_INIT).render({'dkey':dkey,'key':dkey[:4]+' - '+dkey[4:8]+' - '+dkey[8:]}))
        else:
            self.response.write(JINJA_ENV.get_template(DEVICE_MAIN).render({'device':device}))
        #'''
        
        #device.deviceName = u'232호'
        #device.googleCalendarId = 'cs.kookmin.ac.kr_l7ahdck9h1if7qas2gfvl8753s@group.calendar.google.com'
        #self.response.write(JINJA_ENV.get_template(DEVICE_MAIN).render({'device':device}))

class DeviceMethod(webapp2.RequestHandler):
    # access mainpage
    def get(self, dkey, method):
        
        ticVal = time.strftime("%Y%m%d%H",time.localtime());
        
        self.response.headers['Content-Type'] = 'application/json'
            
        device = utils.deviceQuery.selectDeviceWithHashkey(dkey).get()
        status = None
        if device == None :
            deviceAdd(dkey)
            obj = {
                'dKey': dkey,
                'dName': None,
#                'gCalID': None,
                'gCalID': ticVal,
                'status': False,
                'start': '08:00',
                'end': '20:00',
#                'tic': ticVal
            }
            self.response.out.write(json.dumps(obj))
            return
        
        elif device.registeredGroupId == None:
            status = False
        else:
            status = True

        obj = {
            'dKey': device.deviceKey,
            'dName': device.deviceName,
            #'gCalID': device.googleCalendarId,
            'gCalID': ticVal,
            'status': status,
            'start': '08:00',
            'end': '21:00',
            #'tic': ticVal
        }
        self.response.out.write(json.dumps(obj))
        
