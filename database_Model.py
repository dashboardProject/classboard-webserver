from google.appengine.ext import ndb

class User(ndb.Model):
    userId = ndb.StringProperty()
    userLevel = ndb.IntegerProperty(indexed=False)
    lastSignInTime = ndb.DateTimeProperty(auto_now_add=True, indexed=False)
    signUpDate = ndb.DateTimeProperty(auto_now_add=True, indexed=False)

class Group(ndb.Model):
    groupId = ndb.StringProperty()

class GroupMap(ndb.Model):
    userId = ndb.StringProperty()
    groupId = ndb.StringProperty()

class Device(ndb.Model):
    deviceId = ndb.IntegerProperty()
    deviceKey = ndb.IntegerProperty()
    mappedContentId = ndb.IntegerProperty()
    madeUser = ndb.StringProperty()
    madeTime = ndb.DateTimeProperty(auto_now_add=True, indexed=False)

class Content(ndb.Model):
    contentId = ndb.IntegerProperty()
    contentName = ndb.StringProperty(indexed=False)
    googleCalendarId = ndb.StringProperty()
    madeGroupId = ndb.StringProperty()
    madeUserId = ndb.StringProperty()
    madeTime = ndb.DateTimeProperty(auto_now_add=True)