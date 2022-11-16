import Utilities
from SearchCriteria import SearchCriteria
import User

from pprint import pprint


def give_rating(username, rating):
    list = Utilities.getUserlist()
    for user in list:
        if user.username == username:
            user.give_rating(rating)
            break
    Utilities.save(list)

def login(email, pwd):
    userList = Utilities.getUserlist()
    for u in userList:
        print(u.getEmail())
        if (u.email == email):
            return u.loginUser(pwd)
        else:
            return False
def register(email,pwd,vorname,nachname,plz,adress,dob,bio,username,phonenumber,status):
    u = User(email,pwd,vorname,nachname,plz,adress,dob,bio,username,phonenumber,status)
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



if __name__ == '__main__':
    input()
    sc = Utilities.getcurrentSearches()[0]
    pprint(vars(sc))
    help_request = get_filtered_help_request_list(sc)[0]
    input()
    pprint(vars(help_request))
    u1 = Utilities.getUserlist()[0]
    input()
    pprint(vars(u1))
    u1.sendHelpOffer(help_request.id)
    u2 = Utilities.getUserlist()[1]
    input()
    pprint(vars(u2))
    set_match(help_request.id, u1.username)