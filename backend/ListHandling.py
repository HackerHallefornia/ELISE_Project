import Utilities
from SearchCriteria import SearchCriteria
import User
from datetime import date
from HelpRequest import HelpRequest
from pprint import pprint

def get_user_by_username(username:str):
    user_list = Utilities.getUserlist
    for user in user_list:
        if user.username == username:
            break
    return user

def get_help_request_by_id(id:int):
    request_list = Utilities.getHelpRequestslist
    for request in request_list:
        if request.id == id:
            break
    return request

def new_request(own_username:str, category:str, plz:str, deadline:date, starttime:date, endtime:date,description:str ):
    request = HelpRequest(id(),own_username, category, plz, deadline,  starttime, endtime, description)
    Utilities.append_list(request, "Request")

def new_search_criterium(own_username:str, potential_starttime:date, potential_endtime:date, plz, categories):
    crit = SearchCriteria(own_username, potential_starttime, potential_endtime, plz, categories, t=True)
    Utilities.append_list(crit, "SearchCriteria")

def get_potential_matches_for_user(username):
    """
    returns list of [help_request, [potential_matches]]
    """
    request_list = Utilities.getHelpRequestslist()
    help_requests_from_user = []
    for request in request_list:
        if request.username == username:
            potential_matches = get_potential_matches_for_request(request)
            req_with_matches = [request, potential_matches]
            help_requests_from_user.append(req_with_matches)
    return help_requests_from_user

def get_potential_matches_for_request(request_id):
    """
    returns list of helpers
    """
    return get_help_request_by_id(request_id).potential_matches


def get_profile(username):
    """
    returns username and bio
    """
    #TODO interests
    user = get_user_by_username(username)
    return [user.username, user.bio]

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

#     sc = Utilities.getcurrentSearches()[0]
# #    # pprint(vars(sc))
# #     help_request = get_filtered_help_request_list(sc)[0]
# #     pprint(vars(help_request))
# #     # u1 = Utilities.getUserlist()[0]
# #     # input()
# #     # pprint(vars(u1))
# #     # u1.sendHelpOffer(help_request.id)
# #     # u2 = Utilities.getUserlist()[1]
# #     # input()
# #     # pprint(vars(u2))
# #     # print(help_request.id)
# #     # match(help_request.id, u1.username)
# #     # input()
# #     # help_request.cancel_match()