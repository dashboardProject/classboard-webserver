from database_Model import *

def selectDeviceWithId(deviceId):
    return Device.get_by_id(deviceId)

def selectDeviceWithContent(contentId):
    return Device.query(Device.mappedContentId == contentId)

def selectDeviceWithUser(userId):
    return Device.query(Device.madeUser == userId)

def selectDeviceWithGroup(groupId):
    return Device.query().filter(Device.registeredGroupId == groupId)