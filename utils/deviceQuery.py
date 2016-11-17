from database_Model import *

def selectDeviceWithId(deviceId):
    return Device.query(Device.deviceId == deviceId)

def selectDeviceWithContent(contentId):
    return Device.query(Device.mappedContentId == contentId)

def selectDeviceWithUser(userId):
    return Device.query(Device.madeUser == userId)