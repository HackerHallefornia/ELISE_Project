import json
from User import User
from collections import namedtuple
from HelpRequest import HelpRequest
from SearchCriteria import SearchCriteria
#from json import JSONEncoder


def loadJsonAsString(filepath):
    with open(filepath, "r") as read_file:
        data = json.load(read_file)
        jsonString = json.dumps(data)
        return jsonString


def JsonToObjectlist(filepath):
    userString = loadJsonAsString(filepath)
    return json.loads(userString, object_hook=customUserDecoder)


def getcurrentSearches():
    jsonList = JsonToObjectlist("data/CurrentSearches.json")
    listofSearches = []
    for Search in jsonList.Searches:
        Searchinstance = SearchCriteria(Search.Username,
                                      Search.time_start,
                                      Search.time_end,
                                      Search.PLZ,
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
                                      decode_list(Request.potential_matches))
        listofHelpRequests.append(Requestinstance)
    return listofHelpRequests


def decode_list(stringlist):
    chunks = stringlist.split(',')
    return chunks


def getUserlist():
    jsonList = JsonToObjectlist("data/User.json")
    listOfUsers = []
    for user in jsonList.User:
        userinstance = User(user.Email,
                            user.Password,
                            user.FirstName,
                            user.LastName,
                            user.PLZ,
                            user.Adress,
                            user.Birthdate,
                            user.Rating,
                            user.Bio,
                            user.Username,
                            user.Phonenumber,
                            user.Status)
        listOfUsers.append(userinstance)
    return listOfUsers


def customUserDecoder(UserDict):
    return namedtuple('User', UserDict.keys())(*UserDict.values())


def save(Objectlist, JSON_name= "User" ,  filepath="data/test.json"):
    results = [obj.to_json() for obj in Objectlist]
    jsdata = json.dumps({JSON_name : results}, indent=4)
    with open(filepath, 'w') as outfile:
        outfile.write(jsdata)

    print("Data saved")


if __name__ == "__main__":

    # userlist = getUserlist()
    # print(type(userlist))
    # print(userlist[0].username)
    # print(userlist[0].status)
    requestlist = getHelpRequestslist()
    print(requestlist[0].description)
    print(requestlist[0].potential_matches)
    print(requestlist[0].to_json())
    save(requestlist, "Requests", "data/testrequests.json")
    # searches = getcurrentSearches()
    # print(searches[0].categories)
    
