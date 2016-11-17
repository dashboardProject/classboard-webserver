from database_Model import *

def selectContentWithId(contentId):
    return Content.query(Content.contentId == contentId)

def selectContentWithName(contentName):
    return Content.query(Content.contentName == contentName)

def selectContentWithCalendar(calendarId):
    return Content.query(Content.googleCalendarId == calendarId)

def selectContentWithGroup(groupId):
    return Content.query(Content.madeGroupId == groupId)

def selectContentWithUser(userId):
    return Content.query(Content.madeUserId == userId)