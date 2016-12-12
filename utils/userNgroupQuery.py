from database_Model import *
#selectUser('t@t.t').get().key.id()
def selectUser(userMail):
    return User.query(User.userMail == userMail)

def selectGroup(groupName, groupId = None):
    if groupId:
        return Group.get_by_id(groupId)

    return Group.query(Group.groupName == groupName)

def selectUsersInGroup(groupId):
    return GroupMap.query(GroupMap.groupId == groupId)

def selectGroupsOfUser(userMail):
    return GroupMap.query(GroupMap.userMail == userMail)