import json
from User import User
from collections import namedtuple
#from json import JSONEncoder

def loadJsonAsString():
    with open("data/User.json", "r") as read_file:
        data = json.load(read_file)
        jsonString =json.dumps(data)
        return jsonString
    
def JsonToObjectlist():
    userString= loadJsonAsString()
    return json.loads(userString, object_hook=customUserDecoder)

def getUserlist():
    jsonList = JsonToObjectlist()
    listOfUsers =[]
    for user in jsonList.User:
        userinstance = User(user.Email, user.Password,user.FirstName,
                            user.LastName,user.PLZ, user.Birthdate, user.Rating,
                            user.Bio,user.Username,user.NumberRatings) 
        listOfUsers.append(userinstance)
    return listOfUsers
def customUserDecoder(UserDict):
    return namedtuple('User', UserDict.keys())(*UserDict.values())



def save():
    return 0

if __name__ == "__main__":

    userlist = getUserlist()
    print(type(userlist))
    print(userlist[0].email)
