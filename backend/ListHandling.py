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

def add_offer_to_request(helper_username, request_id):
    list = Utilities.getHelpRequestslist()
    for l in list:
        if l.id == request_id:
            l.addPotentialMatch(helper_username)

def filter_help_request_list (search_criteria):
    pass
