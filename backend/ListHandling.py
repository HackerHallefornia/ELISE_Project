import Utilities
from User import User

def login(e, p):
    userList = Utilities.getUserlist()
    for u in userList:
        print(u.getEmail())
        if (u.email == e):
            return u.loginUser(p)
        else:
            return False
def register(e,pwd,v,n,p,a,d,r,b,u,ph,st):
    u = User(e,pwd,v,n,p,a,d,r,b,u,ph,st)
    userList = Utilities.getUserlist()
    userList.append(u)
    Utilities.save(userList)

def addToUserList(u):
    l = getUserList()
    l.append(u)
    l.saveUserList()

def addToPotentialMatchesList(u):
    l = getPotentialMatchesList()
    l.append(u)
    l.savePotentialMatchesList()

register("johannes.boldt@freenet.de", "Passwort123", "Johannes", "Boldt2", "06108", "Hauptstrasse 2", "1967-01-01", "0", "Hallo, ich bins. Ich mag walks in the park.", "johannesboldt2", "110", "Helper")