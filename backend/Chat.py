import datetime
class Chat():
    def __init__(self, username1, username2, messages = [], u1_phone = "Hidden", u2_phone = "Hidden", u1_adress= "Hidden", u2_adress = "Hidden"):
        self.user1 = username1
        self.user2 = username2
        self.messages = messages
        self.u1_phone = u1_phone
        self.u2_phone = u2_phone
        self.u1_adress = u1_adress
        self.u2_adress = u1_adress


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
        if (username == self.user1):
            self.u1_adress == "Visible"
        if (username == self.user2):
            self.u2_adress == "Visible"

class Message():
    def __init__(self, sender, content, time = datetime.now()):
        self.sender = sender
        self.content = content

def getMessagesForChat():
    #TODO
    pass

def getChatsForUser():
    #TODO
    pass

