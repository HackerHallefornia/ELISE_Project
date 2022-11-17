import Utilities
from SearchCriteria import SearchCriteria
import User
from datetime import date

from pprint import pprint

def give_rating(username: str, rating: int):
    """
    give rating to a specific user
    """
    list = Utilities.getUserlist()
    for user in list:
        if user.username == username:
            user.give_rating(rating)
            break
    Utilities.save(list)

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
    Utilities.save(userList)

def addToUserList(u:User):
    """
    adds user to list of users and saves to json
    """
    list = Utilities.getUserList()
    list.append(u)
    list.saveUserList()

def add_offer_to_request(helper_username:str, request_id:int):
    """
    add help offer as potential match to a help request
    """
    list = Utilities.getHelpRequestslist()
    for request in list:
        if request.id == request_id:
            request.addPotentialMatch(helper_username)
            break
    Utilities.save(list, 'Requests', 'data/testrequests.json')

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

def set_match(request_id, helper_username):
    """
    set match of a specific helper to a help request
    """
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