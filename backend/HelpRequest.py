from datetime import datetime
import HelpOffer
class HelpRequest():
    category =""
    plz = ""
    deadline = datetime(1900,1,1)
    description =""
    match : HelpOffer
    potential_matches = HelpOffer[100]
    active = True
    visible = True
    startingtime = datetime(1900,1,1)
    endtime = datetime(1900,1,1)

    def __init__(self, c, p, d,t,  desc):
        self.category = c
        self.plz = p
        self.deadline = d
        self.description = desc
        self.time = t

    def setMatch(h):
        match = h

    def addPotentialMatch():
        # speichern in json
        pass
    
    def loadPotentialMatches():
        #laden aus der json
        pass

    def setCategory(self, c):
        self.category = c
        return True
    def getCategory(self):
        return self.category
    def getActive(self):
        return self.active
    def getVisible(self):
        return self.visible
    def getDeadline(self):
        return self.deadline
    def getStartingTime(self):
        return self.startingtime
    def getEndTime(self):
        return self.endtime
    def getPLZ(self):
        return self.plz