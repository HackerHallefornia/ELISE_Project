from Utilities import getUserList, getPotentialMatchesList, saveUserList, savePotentialMatchesList

def login(e, p):
    userList = loadUsers()
    for u in userList:
        if (u.getEmail == e):
            return u.loginUser(p)
        else:
            return False

def addToUserList(u):
    l = getUserList()
    l.append(u)
    l.saveUserList()

def addToPotentialMatchesList(u):
    l = getPotentialMatchesList()
    l.append(u)
    l.savePotentialMatchesList()