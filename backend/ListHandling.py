import Utilities

def login(e, p):
    userList = Utilities.getUserlist()
    for u in userList:
        print(u.getEmail())
        if (u.email == e):
            return u.loginUser(p)
        else:
            return False

# def addToUserList(u):
#     l = getUserList()
#     l.append(u)
#     l.saveUserList()

# def addToPotentialMatchesList(u):
#     l = getPotentialMatchesList()
#     l.append(u)
#     l.savePotentialMatchesList()