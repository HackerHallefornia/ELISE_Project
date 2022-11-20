from backend import Utilities
from backend.SearchCriteria import SearchCriteria
from backend.User import User
from datetime import date


def get_chat_id_by_usernames(username1:str, username2:str):
    chatList= Utilities.getChatlist()
    for chat in chatList:
        if (username1 == chat.user1 or username1 == chat.user2):
            if (username2 == chat.user1 or username2 == chat.user2):
                u = chat
    try:
        return u.id
    except NameError:
        return False
def get_messages_for_chat(username1, username2):
    """
    returns all Messages for chat between two users, returns False if it does not exist
    """
    chat_id = get_chat_id_by_usernames(username1, username2)
    return Utilities.getMessageListForChat(chat_id)

def get_new_messages_for_chat(username1, username2):
    """
    returns all unseen Messages for chat between two users
    """
    message_list = get_messages_for_chat(username1, username2)
    unseen_messages = []
    for message in message_list:
        if message.seen == False:
            unseen_messages.append(message)
    return unseen_messages

def get_new_messages_for_user(username):
    chats = get_chats_for_user(username)
    new_messages = []
    for chat in chats:
        new_messages_chat = get_new_messages_for_chat(chat.user1, chat.user2)
        list_element = [chat, new_messages_chat]
        new_messages.append(list_element)
    return new_messages

def get_chats_for_user(username):
    """
    TODO
    returns all chat_ids of a user
    """
    chatList= Utilities.getChatlist()
    chat_id_list = []
    for chat in chatList:
        if(username == chat.user1) or (username == chat.user2):
            chat_id_list.append(chat.id)
    return chat_id_list

def new_chat(username_sender:str, username_receiver:str):
    """
    creates new chat from two usernames
    """
    chat = Chat(username_sender, username_receiver)
    Utilities.append_list(chat, "Chat")
    Utilities.createChatFile(chat)



def send_message(username_sender:str, username_receiver:str, content:str):
    """
    send message from sender to receiver. If chat does not exist, net chat gets created
    """
    chat = get_chat_id_by_usernames(username_sender, username_receiver)
    print(chat)
    if chat == False:
        new_chat(username_sender, username_receiver)
    chat = get_chat_id_by_usernames(username_sender, username_receiver)
    message = Message(username_sender, content, datetime.now())
    Utilities.append_list(message, "Message", chat)
        
def sendPhoneNumber(sender, receiver):
    """
    returns false if no phone number is saved
    """
    user = get_user_by_username(sender)
    if user == False:
        return user
    else:
        Chat.send_message(sender, receiver, "Meine Telefonnummer ist" + str(user.phonenumber))
        return True

def sendAdress(sender, receiver):
    """
    returns false if no address is saved
    """
    user = get_user_by_username(sender)
    if user == False:
        return user
    else:
        send_message(sender, receiver, "Meine Adresse ist" + str(user.adress))
        return True

def get_user_by_username(username:str):
    user_list = Utilities.getUserlist()
    condition = False
    for user in user_list:
        if user.username == username:
            condition = True
            break
    if condition:
        return user
    else:
        return condition

def get_help_request_by_id(id:int):
    request_list = Utilities.getHelpRequestslist()
    condition = False
    for request in request_list:
        if request.id == id:
            condition = True
            break
    if condition:
        return request
    else:
        return condition

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
            return [u.loginUser(pwd), u.username]
        else:
            return False

def register(email:str,pwd:str,vorname:str,
    nachname:str,plz:str,dob:str,
    username:str,
    phonenumber= " ",adress= "no address", bio= " ", status= "Helper"):
    """
    register user to website
    """
    u = User(email,pwd,vorname,nachname,plz,adress,dob,bio,username,phonenumber,status)
    addToUserList(u)

def addToUserList(u:User):
    """
    adds user to list of users and saves to json
    """
    userlist = Utilities.getUserlist()
    userlist.append(u)
    Utilities.save(userlist, "User", "/home/PaTe/mysite/data/User.json")

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

def get_filtered_help_request_list(search_criteria : SearchCriteria):
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

    sc = Utilities.getcurrentSearches()[0]
   # pprint(vars(sc))
    help_request = get_filtered_help_request_list(sc)[0]
    pprint(vars(help_request))
    # u1 = Utilities.getUserlist()[0]
    # input()
    # pprint(vars(u1))
    # u1.sendHelpOffer(help_request.id)
    # u2 = Utilities.getUserlist()[1]
    # input()
    # pprint(vars(u2))
    # print(help_request.id)
    # match(help_request.id, u1.username)
    # input()
    # help_request.cancel_match()
