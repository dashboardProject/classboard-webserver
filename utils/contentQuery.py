from database_Model import *

def selectContentWithId(contentId):
    return Content.query().filter(Content.contentId == contentId)

def selectContentWithName(contentName):
    return Content.query().filter(Content.contentName == contentName)

def selectContentWithCalendar(calendarId):
    return Content.query().filter(Content.googleCalendarId == calendarId)

def selectContentWithGroup(groupId):
    return Content.query().filter(Content.madeGroupId == groupId)

def selectContentWithUser(userId):
    return Content.query().filter(Content.madeUserId == userId)