import Utilities
from SearchCriteria import SearchCriteria
import User

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
    list = Utilities.getUserList()
    list.append(u)
    list.saveUserList()

def add_offer_to_request(helper_username, request_id):
    list = Utilities.getHelpRequestslist()
    for request in list:
        if request.id == request_id:
            request.addPotentialMatch(helper_username)
            break
    Utilities.save(list, 'Requests', 'data/testrequests.json')

def get_filtered_help_request_list (search_criteria : SearchCriteria):
    list = Utilities.getHelpRequestslist()
    filtered_list = []
    for l in list:
        if search_criteria.compare_to_help_request:
            filtered_list.append(l)
    return filtered_list

def set_match(request_id, helper_username):
    list = Utilities.getHelpRequestslist()
    for request in list:
        if request.id == request_id:
            request.setMatch(helper_username)
            break
    Utilities.save(list, 'Requests', 'data/testrequests.json')

# def loadPotentialMatchesUser(username):
#         list = Utilities.getHelpRequestslist()
#         for l in list:
#             if l.id == username:
#                 pass

# def loadPotentialMatchesHelpRequest(request_id):
#    pass 

if __name__ == '__main__':
    sc = Utilities.getcurrentSearches()[0]
    help_request = get_filtered_help_request_list(sc)[0]
    u1 = Utilities.getUserlist()[0]
    u1.sendHelpOffer(help_request.id)
    u2 = Utilities.getUserlist()[1]
    set_match(help_request.id, u1.username)
    print('Its a match')