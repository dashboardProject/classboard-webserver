import json
import time
import webapp2

import logging
from database_Model import Group, GroupMap, Device
from utils.decorators import userCheck
from utils.userNgroupQuery import selectUser, selectGroupsOfUser, selectGroup, selectUsersInGroup, selectMap
from utils.deviceQuery import selectDeviceWithGroup, selectDeviceWithHashkey
from utils.contentQuery import selectContentWithGroup
from google.appengine.api import users, mail
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
            userMail = user.email()
            tempList = selectGroupsOfUser(userMail).fetch()

            groupList = [selectGroup(None, i.groupId) for i in tempList]
            groupList = sorted(groupList, key=lambda i: i.groupName)
            deviceCountList = [selectDeviceWithGroup(i.key.id()).count() for i in groupList]

        except Exception as e:
            groupList = []
            deviceCountList = []

        template_values = {'groupInfo': groupList,
                           'deviceCount': deviceCountList, }

        self.response.write(JINJA_ENV.get_template(MANAGEMENT_PAGE).render(template_values))


class ManagementGroup(webapp2.RequestHandler):
    # access mainpage
    @userCheck
    def get(self, *args):
        # add query and template data
        userData = selectUsersInGroup(int(args[0])).fetch()
        userInfo = [selectUser(i.userMail).get() for i in userData]
        groupName = selectGroup(groupId=int(args[0])).get().groupName

        template_values = {'userInfo': userInfo,
                           'groupId' : int(args[0]),
                           'totalUser' : userData,
                           'groupName' : groupName, }

        self.response.write(JINJA_ENV.get_template(MANAGEMENT_GROUP).render(template_values))


class MakeGroup(webapp2.RequestHandler):
    @userCheck
    def get(self):
        self.response.write(JINJA_ENV.get_template(MAKE_GROUP).render())

    @userCheck
    def post(self):
        user = users.get_current_user()
        userMail = user.email()

        groupName = self.request.get('name')

        if selectGroup(groupName).count() is 0:
            newGroupId = Group(groupName=groupName).put().get().key.id()
            GroupMap(userMail=userMail, groupId=newGroupId).put()

        time.sleep(1)
        self.redirect('/management/%d/group'%(newGroupId), True)


class InvitationUser(webapp2.RequestHandler):
    def post(self, *args):
        data =json.loads(self.request.body)
        invitationMail = data[u'invitationMail']

        if selectGroupsOfUser(invitationMail).filter(GroupMap.groupId == int(args[0])).count() is 0:
            GroupMap(userMail=invitationMail, groupId=int(args[0])).put()

            groupName = selectGroup(None, int(args[0]))

            mail.send_mail(sender='ClassBorad', to=invitationMail, subject='You have been invited to a group.',
                           body="""You have been invited to a group '%s'.
                           http://temp.temp/management/group%d"""%(groupName, int(args[0])))


class GroupRename(webapp2.RequestHandler):
    def get(self, *args):
        gid = int(args[0])
        newName = self.request.get('newName')

        temp = selectGroup(None, groupId=gid)
        temp.groupName = newName
        temp.put()

        time.sleep(1)
        self.redirect('/management/%d/group' % (gid), True)


class SecessionUser(webapp2.RequestHandler):
    def get(self, *args):
        user = users.get_current_user()
        userMail = user.email()
        gid = int(args[0])

        selectMap(userMail, int(gid)).get().key.delete()

        if selectUsersInGroup(gid).count() is 0:
            selectDeviceWithGroup(gid).fetch().key.delete()
            selectContentWithGroup(gid).fetch().key.delete()

        time.sleep(1)

        self.redirect_to('management')


class ManagementDevice(webapp2.RequestHandler):
    # access mainpage
    @userCheck
    def get(self, *args):
        # add query and template data
        deviceInfo = selectDeviceWithGroup(args[0]).get()
        groupName = selectGroup(groupId=int(args[0])).get().groupName

        emplate_values = {'userInfo': deviceInfo,
                          'groupId': int(args[0]),
                          'groupName': groupName, }

        self.response.write(JINJA_ENV.get_template(MANAGEMENT_DEVICE).render())


class AddDevice(webapp2.RequestHandler):
    @userCheck
    def post(self, *args):
        user = users.get_current_user()
        userMail = user.email()

        gid = int(args[0])
        deviceName = args[1]
        hashKey = args[2]
        contentId = args[3] if len(args[3]) > 0 else None

        temp = selectDeviceWithHashkey(hashKey).get()
        temp.deviceName = deviceName
        temp.googleCalendarId = contentId
        temp.registeredGroupId = gid
        temp.registeredUser = userMail

        temp.put()


class ModifiedDevice(webapp2.RequestHandler):
    @userCheck
    def post(self,*args):
        user = users.get_current_user()
        userMail = user.email()

        gid = int(args[0])
        deviceName = args[1]
        hashKey = args[2]
        contentId = args[3] if len(args[3]) > 0 else None

        temp = selectDeviceWithHashkey(hashKey).get()
        temp.deviceName = deviceName
        temp.googleCalendarId = contentId
        temp.put()





# class ManagementContents(webapp2.RequestHandler):
#     # access mainpage
#     @userCheck
#     def get(self):
#         # add query and template data
#         self.response.write(JINJA_ENV.get_template(MANAGEMENT_CONTENTS).render())

