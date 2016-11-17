from google.appengine.ext import ndb

class User(ndb.Model):
    userMail = ndb.StringProperty()
    userLevel = ndb.IntegerProperty(indexed=False)
    lastSignInTime = ndb.DateTimeProperty(auto_now_add=True, indexed=False)
    signUpDate = ndb.DateTimeProperty(auto_now_add=True, indexed=False)

class Group(ndb.Model):
    groupName = ndb.StringProperty()

class GroupMap(ndb.Model):
    userId = ndb.StringProperty()
    groupId = ndb.StringProperty()

class Device(ndb.Model):
    deviceKey = ndb.IntegerProperty()
    mappedContentId = ndb.IntegerProperty()
    madeUser = ndb.StringProperty()
    madeTime = ndb.DateTimeProperty(auto_now_add=True, indexed=False)

class Content(ndb.Model):
    contentName = ndb.StringProperty()
    googleCalendarId = ndb.StringProperty()
    madeGroupId = ndb.StringProperty()
    madeUserId = ndb.StringProperty()
    madeTime = ndb.DateTimeProperty(auto_now_add=True)