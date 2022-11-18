import backend.Utilities as Utilities


class Chat():

    
    def __init__(self, username1:str, username2:str, Id = ""):
        
        self.user1 = username1
        self.user2 = username2
        self.id = Id
        if self.id == "":
            self.id = str(hash(username1+username1))[1:13]
            
    def addMessageToChat(self,message):
        self.messages.append(message)

    def sendPhoneNumber(username, self):
        if (username == self.user1):
            self.u1_phone == "Visible"
        if (username == self.user2):
            self.u2_phone == "Visible"

    def sendAdress(username, self):
        """
        returns false if no address is saved
        """

    def to_json(self):
        return {"user1":self.user1,
                "user2":self.user2, 
                "self.id":self.id
                }

        

class Message():
    def __init__(self, sender, receiver, content, time):

        self.sender = sender
        self.content = content

def getMessagesForChat(Chat, username):
    #TODO
    pass

def getChatsForUser():
    #TODO
    pass

if __name__ == '__main__':
    
    chat1 = Chat("johnnyboi", "elma")
    print(chat1.id)
    Chatlist = [chat1, Chat("emma", "annemarie")]
    Utilities.save(Chatlist,"Chats", "data/Chats.json")
    