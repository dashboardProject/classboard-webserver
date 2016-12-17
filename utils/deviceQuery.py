from database_Model import *

def selectDeviceWithId(deviceId):
    return Device.get_by_id(deviceId)

def selectDeviceWithName(deviceName):
    return Device.query(Device.deviceName == deviceName)

def selectDeviceWithContent(contentId):
    return Device.query(Device.googleCalendarId == contentId) #Device.query(Device.mappedContentId == contentId)

def selectDeviceWithUser(userId):
    return Device.query(Device.madeUser == userId)

def selectDeviceWithGroup(groupId):
    return Device.query().filter(Device.registeredGroupId == groupId)