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



def save(Userlist, filepath="data/test.json"):
    results = [obj.to_json() for obj in Userlist]
    jsdata = json.dumps({"User": results}, indent=4)
    with open(filepath, 'w') as outfile:
        outfile.write(jsdata)
    
    print("Data saved")

if __name__ == "__main__":

    userlist = getUserlist()
    print(type(userlist))
    print(userlist[0].username)
    print(userlist[0].status)
    save(userlist)