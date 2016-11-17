from database_Model import *

def selectDeviceWithId(deviceId):
    return Device.query().filter(Device.deviceId == deviceId)

def selectDeviceWithContent(contentId):
    return Device.query().filter(Device.mappedContentId == contentId)

def selectDeviceWithUser(userId):
    return Device.query().filter(Device.madeUser == userId)