from datetime import datetime
import backend.ListHandling as ListHandling
import backend.Utilities as Utilities

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


    def __init__(self, id, username, category, plz, deadline,description ,starttime, endtime,  po = [], match = '', status='Active'):

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
        self.status = status
        
    
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
        request_list = Utilities.getHelpRequestslist()
        Utilities.updateRequestInRequestlist(request_list, self)


    def complete_request(self,rating, username_to_rate):
        user_list = Utilities.getUserlist()
        # get corresponding user to username
        for u in user_list:
            if u.username == username_to_rate:
                break
        if username_to_rate == self.match:
            # means you are the creator of HelpRequest
            u.give_rating(rating)
            self.status = 'Fulfilled'
            print(vars(self))
            request_list = Utilities.getHelpRequestslist()
            Utilities.updateRequestInRequestlist(request_list, self)
            

        if username_to_rate == self.username:
            #means you are the helper 
            if self.status == 'Fulfilled':
                u.give_rating(rating)
            else:
                return False

    def cancel_match(self, status="Active"):
        self.match = ""
        self.status = status
        request_list = Utilities.getHelpRequestslist()
        Utilities.updateRequestInRequestlist(request_list, self)

    def addPotentialMatch(self, helper_username):
        self.potential_matches.append(helper_username)