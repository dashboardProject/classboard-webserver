from database_Model import *

def selectUser(userId):
    return User.query(User.userId == userId)

def selectGroup(groupId):
    return Group.query(Group.groupId == groupId)

def selectUsersInGroup(groupId):
    return GroupMap.query(GroupMap.groupId == groupId)

def selectGroupsOfUser(userId):
    return GroupMap.query(GroupMap.userId == userId)