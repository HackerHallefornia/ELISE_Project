from datetime import datetime
import Utilities

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

    def __init__(self, category, plz, deadline,time,description, po = [], i=id()):
        self.id = i
        self.category = category
        self.plz = plz
        self.deadline = deadline
        self.description = description
        self.time = time
        self.potential_matches = po
        
    def setMatch(self,helper_username):
        self.match = helper_username
        self.status = "Matched"


    def addPotentialMatch(self, helper_username):
        self.potential_matches.append(helper_username)
                
    def loadPotentialMatches(self):
        list = Utilities.getHelpRequestslist()
        for l in list:
            if l.id == self.id:
                self.potential_matches = l.potential_matches