import json
import webapp2

import logging
from database_Model import Group, GroupMap
from utils.decorators import userCheck
from utils.userNgroupQuery import selectUser, selectGroupsOfUser, selectGroup, selectUsersInGroup
from utils.deviceQuery import selectDeviceWithGroup
from google.appengine.api import users
from configs import JINJA_ENV, TUTORIAL_PAGE, MANAGEMENT_PAGE,MANAGEMENT_CONTENTS,\
                      MANAGEMENT_GROUP, MANAGEMENT_DEVICE, DEVICE_MAIN, MAKE_GROUP


class Tutorial(webapp2.RequestHandler):
    # access mainpage
    def get(self):
        # add query and template data
        self.response.write(JINJA_ENV.get_template(TUTORIAL_PAGE).render())


class Management(webapp2.RequestHandler):
    # access mainpage
    @userCheck
    def get(self):
        try:
            user = users.get_current_user()
            userId = selectUser(user.email()).get().key.id()
            tempList = selectGroupsOfUser(userId).fetch()

            groupList = [selectGroup(None, i.groupId) for i in tempList]
            groupList = sorted(groupList, key=lambda i:i.groupName)
            deviceCountList = [selectDeviceWithGroup(i.key.id()).count() for i in groupList]

        except Exception as e:
            groupList = []
            deviceCountList = []

        template_values = {'groupInfo' : groupList,
                           'deviceCount' : deviceCountList,}

        self.response.write(JINJA_ENV.get_template(MANAGEMENT_PAGE).render(template_values))


class MakeGroup(webapp2.RequestHandler):
    @userCheck
    def get(self):
        self.response.write(JINJA_ENV.get_template(MAKE_GROUP).render())

    @userCheck
    def post(self):
        user = users.get_current_user()
        userId = selectUser(user.email()).get().key.id()

        groupName = self.request.get('name')

        if selectGroup(groupName).count() is 0:
            newGroupId = Group(groupName = groupName).put().get().key.id()
            GroupMap(userId = userId, groupId = newGroupId).put()

            self.redirect('/management/group%d'%(newGroupId), True)


class ManagementGroup(webapp2.RequestHandler):
    # access mainpage
    @userCheck
    def get(self, *args):
        # add query and template data
        userInfo = selectUsersInGroup(int(args[0])).fetch()
        
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