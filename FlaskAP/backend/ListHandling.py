from backend import Utilities
from SearchCriteria import SearchCriteria
import User
from datetime import date
from HelpRequest import HelpRequest

from pprint import pprint



def login(email:str, pwd:str):
    """
    log into website
    returns false if login failed
    """
    userList = Utilities.getUserlist()
    for u in userList:
        print(u.getEmail())
        if (u.email == email):
            return u.loginUser(pwd)
        else:
            return False

def register(email:str,pwd:str,vorname:str,nachname:str,plz:str,adress:str,dob:date,bio:str,username:str,phonenumber:str,status:str):
    """
    register user to website
    """
    u = User(email,pwd,vorname,nachname,plz,adress,dob,bio,username,phonenumber,status)
    userList = Utilities.getUserlist()
    userList.append(u)
    Utilities.save(list, "User", "data/User.json")

def addToUserList(u:User):
    """
    adds user to list of users and saves to json
    """
    list = Utilities.getUserList()
    list.append(u)
    Utilities.save(list, "User", "data/User.json")

def add_offer_to_request(helper_username:str, request_id:int):
    """
    add help offer as potential match to a help request
    """
    list = Utilities.getHelpRequestslist()
    for request in list:
        if request.id == request_id:
            request.addPotentialMatch(helper_username)
            break
    Utilities.save(list, 'Requests', 'data/HelpRequests.json')

def get_filtered_help_request_list (search_criteria : SearchCriteria):
    """
    returns help requests list with filtered results for search criteria
    """
    list = Utilities.getHelpRequestslist()
    filtered_list = []
    for l in list:
        if search_criteria.compare_to_help_request:
            filtered_list.append(l)
    return filtered_list

def match(request_id, helper_username):
    """
    set match of a specific helper to a help request
    """
    list = Utilities.getHelpRequestslist()
    for request in list:
        if request.id == request_id:
            request.setMatch(helper_username)
            break
    Utilities.save(list, 'Requests', 'data/HelpRequests.json')

def give_rating(username_to_rate: str, rating: int, help_request : HelpRequest):
    """
    give rating to a specific user, helpseeker has to give rating first and close request
    """
    request_list = Utilities.getHelpRequestslist()
    for request in request_list:
        if help_request.id == request.id:
            help_request.complete_request(rating, username_to_rate)
            break

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
    print(help_request.id)
    match(help_request.id, u1.username)
    input()
    help_request.cancel_match()