import datetime
class Chat():
    def __init__(self, username1, username2, messages = []):
        self.user1 = username1
        self.user2 = username2
        self.messages = messages

    def addMessageToChat(self,message):
        self.messages.append(message)

    def sendPhoneNumber():
        """
        returns false if no phone number saved
        """
        pass

    def sendAdress():
        """
        returns false if no address is saved
        """

class Message():
    def __init__(self, sender, receiver, content, time = datetime.now(), id=id()):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.id = id

def getMessagesForChat():
    #TODO
    pass

def getChatsForUser():
    #TODO
    pass

