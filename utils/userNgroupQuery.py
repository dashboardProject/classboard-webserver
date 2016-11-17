from database_Model import *

def selectUser(userMail):
    return User.query(User.userMail == userMail)

def selectGroup(groupName):
    return Group.query(Group.groupName == groupName)

def selectUsersInGroup(groupId):
    return GroupMap.query(GroupMap.groupId == groupId)

def selectGroupsOfUser(userId):
    return GroupMap.query(GroupMap.userId == userId)