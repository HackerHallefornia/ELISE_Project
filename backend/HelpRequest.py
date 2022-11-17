from datetime import datetime
import ListHandling

class HelpRequest():
    id = 0
    username = ""
    category =""
    plz = ""
    deadline = datetime(1900,1,1)
    description =""
    match = ""
    status =  "Active" # Active, Matched, Fulfilled
    startingtime = datetime(1900,1,1)
    endtime = datetime(1900,1,1)
    potential_matches = []

    def __init__(self, username, category, plz, deadline,description ,starttime, endtime, po = [], match = '', status='Active', id = id):
        self.id = id
        self.username = username
        self.category = category
        self.plz = plz
        self.deadline = deadline
        self.description = description
        self.startingtime = starttime
        self.endtime = endtime
        self.potential_matches = po
        self.status= status
        self.match = match
    
    def to_json(self):
        return {"ID":self.id,
            "Username":self.username,
            "subcategory":self.category, 
            "category":self.category, 
            "deadline":self.deadline,
            "PLZ":self.plz,
            "time_start":self.startingtime,
            "time_end":self.endtime,
            "description":self.description,
            "potential_matches": ",".join(self.potential_matches),
            "match": self.match,
            "status": self.status
            }
        
    def setMatch(self, helper_username):
        self.match = helper_username
        self.status = "Matched"

    def complete_request(self,rating, username, user_status):
        if user_status == 'Helper':
            if self.status == 'Fulfilled':
                ListHandling.give_rating(self.username, rating)
            else:
                return False
        if user_status == 'HelpSeeker':
            self.status == 'Fulfilled'
            ListHandling.give_rating(self.match, rating)


    def cancel_match(self, status="Active"):
        self.match = ""
        self.status = status

    def addPotentialMatch(self, helper_username):
        self.potential_matches.append(helper_username)