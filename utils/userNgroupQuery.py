from database_Model import *
#selectUser('t@t.t').get().key.id()
def selectUser(userMail):
    return User.query().filter(User.userMail == userMail)

def selectGroup(groupName):
    return Group.query().filter(Group.groupName == groupName)

def selectUsersInGroup(groupId):
    return GroupMap.query().filter(GroupMap.groupId == groupId)

def selectGroupsOfUser(userId):
    return GroupMap.query().filter(GroupMap.userId == userId)