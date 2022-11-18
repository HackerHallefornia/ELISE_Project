import json
import User
from collections import namedtuple
from HelpRequest import HelpRequest
from SearchCriteria import SearchCriteria
from Chat import Chat, Message
#from json import JSONEncoder


def loadJsonAsString(filepath):
    with open(filepath, "r") as read_file:
        data = json.load(read_file)
        jsonString = json.dumps(data)
        return jsonString


def JsonToObjectlist(filepath):
    userString = loadJsonAsString(filepath)
    return json.loads(userString, object_hook=customUserDecoder)

def getMessageListForChat(chatId:str):
    filepath = "data/chats/" + chatId + ".json"
    jsonList = JsonToObjectlist(filepath)
    list_of_messages = []
    for message in jsonList.Chat:
        message_instance = Message(message.sender,
                                message.content,
                                message.time,
                                message.seen)
        list_of_messages.append(message_instance)  
    return list_of_messages  

def getcurrentSearches():
    jsonList = JsonToObjectlist("data/CurrentSearches.json")
    listofSearches = []
    for Search in jsonList.Searches:
        Searchinstance = SearchCriteria(Search.Username,
                                      Search.time_start,
                                      Search.time_end,
                                      decode_list(Search.PLZ),
                                      decode_list(Search.categories),
                                      Search.timeframe)
        listofSearches.append(Searchinstance)
    return listofSearches


def getHelpRequestslist():
    jsonList = JsonToObjectlist("data/HelpRequests.json")
    listofHelpRequests = []
    for Request in jsonList.Requests:
        Requestinstance = HelpRequest(Request.ID,
                                      Request.Username,
                                      Request.category,
                                      Request.PLZ,
                                      Request.deadline,
                                      Request.description,
                                      Request.time_start,
                                      Request.time_end,
                                      decode_list(Request.potential_matches),
                                      Request.match
                                      )
        listofHelpRequests.append(Requestinstance)
    return listofHelpRequests

def getChatlist():
    jsonList = JsonToObjectlist("data/Chats.json")
    Chatslist = []
    for chat in jsonList.Chats:
        ChatInstance = Chat(chat.user1,
                            chat.user2,
                            chat.id)
        Chatslist.append(ChatInstance)
    return Chatslist

def decode_list(stringlist):
    chunks = stringlist.split(',')
    return chunks


def getUserlist():
    jsonList = JsonToObjectlist("data/User.json")
    listOfUsers = []
    for user in jsonList.User:
        userinstance = User.User(user.Email,
                            user.Password,
                            user.FirstName,
                            user.LastName,
                            user.PLZ,
                            user.Adress,
                            user.Birthdate,
                            user.Bio,
                            user.Username,
                            user.Phonenumber,
                            user.Status,
                            user.NumberRatings,
                            user.Rating)
        listOfUsers.append(userinstance)
    return listOfUsers

def updateUserInUserlist(Userlist, changedUser):
    for i in range(len(Userlist)):
        if Userlist[i].username == changedUser.username:
            Userlist[i] = changedUser
    save(Userlist, "User", "data/User.json")

def updateRequestInRequestlist(requestList, changedRequest):
    for i in range(len(requestList)):
        if requestList[i].id == changedRequest.id:
            requestList[i] = changedRequest
    save(requestList, "Requests", "data/HelpRequests.json")



def append_list(new_obj:object, type:str, id:str = ""):
    """
    parameter type is either User, SearchCriteria or Request, Chat, Message
    """
    if type == "User":
        userList = getUserlist()
        userList.append(new_obj)
        save(userList, "User", "data/User.json")
    if type == "Request":
        requestList = getHelpRequestslist
        requestList.append(new_obj)
        save(requestList, "Requests", "data/HelpRequests.json")
    if type == "SearchCriteria":
        critList = getcurrentSearches()
        critList.append(new_obj)
        save(critList, "Searches", "data/CurrentSearches.json")
    if type == "Chat":
        chatList = getChatlist()
        chatList.append(new_obj)
        save(chatList, "Chats", "data/Chats.json")
    if type == "Message":
        messageList = getMessageListForChat(id)
        messageList.append(new_obj)
        filepath = "data/chats/" + id + ".json"
        save(messageList, "Chat", filepath)
    
def customUserDecoder(UserDict):
    return namedtuple('User', UserDict.keys())(*UserDict.values())


def save(Objectlist, JSON_name= "User" ,  filepath="data/test.json"):
    results = [obj.to_json() for obj in Objectlist]
    jsdata = json.dumps({JSON_name : results}, indent=4)
    with open(filepath, 'w') as outfile:
        outfile.write(jsdata)
    print("Data saved")

def save_empty(Objectlist, JSON_name= "User" ,  filepath="data/test.json"):
    results = [obj.to_json() for obj in Objectlist]
    jsdata = json.dumps({JSON_name : results}, indent=4)
    with open(filepath, 'a+') as outfile:
        outfile.write(jsdata)
    print("Data saved")

def createChatFile(chat:Chat):
    filepath = "data/chats/" + chat.id + '.json'
    list = []
    save_empty(list, "Chat", filepath)

if __name__ == "__main__":

    # userlist = getUserlist()
    # print(type(userlist))
    # print(userlist[0].username)
    # print(userlist[0].status)
    # requestlist = getHelpRequestslist()
    # print(requestlist[0].description)
    # print(requestlist[0].potential_matches)
    # print(requestlist[0].to_json())
    # save(requestlist, "Requests", "data/testrequests.json")
    searches = getcurrentSearches()
    print(searches[0].categories)
    print(searches[0].plz)
    print(searches[0].to_json())
    save(searches, "Searches", "data/testsearches.json")
