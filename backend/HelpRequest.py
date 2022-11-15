from datetime import datetime
import HelpOffer
class HelpRequest():
    category =""
    plz = ""
    deadline = datetime(1900,1,1)
    description =""
    match = []
    potential_matches = []
    active = True
    visible = True

    def __init__(self, c, p, d, desc):
        self.category = c
        self.plz = p
        self.deadline = d
        self.description = desc
    
    def setMatch():
        match = 0

    def addPotentialMatch():
        # speichern in json
        pass
    
    def loadPotentialMatches():
        #laden aus der json
        pass