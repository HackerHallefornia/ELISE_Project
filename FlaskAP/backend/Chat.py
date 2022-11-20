from datetime import time, datetime

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
    def __init__(self, sender, content, time:datetime , seen=False):

        self.sender = sender
        self.content = content
        self.time = time
        self.seen = seen

    def to_json(self):
        return {
            "sender": self.sender,
            "content": self.content,
            "time": str(self.time),
            "seen": self.seen
        }



            
if __name__ == '__main__':
    print(get_new_messages_for_user("konrad"))