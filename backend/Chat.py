import Utilities
import ListHandling
from datetime import time

class Chat():

    
    def __init__(self, username1:str, username2:str, id = ""):
        
        self.user1 = username1
        self.user2 = username2
        self.id = id
        if self.id == "":
            self.id = str(hash(username1+username2))[1:13]

    def to_json(self):
        return {"user1":self.user1,
                "user2":self.user2, 
                "id":self.id
                }

        

class Message():
    def __init__(self, sender, content, time , seen=False):

        self.sender = sender
        self.content = content
        self.time = time
        self.seen = seen

    def to_json(self):
        return {
            "sender": self.sender,
            "content": self.content,
            "time": self.time,
            "seen": self.seen
        }

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
    message = Message(username_sender, username_receiver, content)
    Utilities.append_list(message, "Message", chat)
        
def sendPhoneNumber(sender, receiver):
    """
    returns false if no phone number is saved
    """
    user = ListHandling.get_user_by_username(sender)
    if user == False:
        return user
    else:
        send_message(sender, receiver, "Meine Telefonnummer ist" + str(user.phonenumber))
        return True

def sendAdress(sender, receiver):
    """
    returns false if no address is saved
    """
    user = ListHandling.get_user_by_username(sender)
    if user == False:
        return user
    else:
        send_message(sender, receiver, "Meine Adresse ist" + str(user.adress))
        return True

if __name__ == '__main__':
    print(get_new_messages_for_user("konrad"))