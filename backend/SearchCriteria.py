from datetime import datetime
import HelpRequest
class SearchCriteria():
    startingpoint = datetime(1900,1,1,12,0)
    endpoint = datetime(1900,1,1,12,0)
    timeframe = False
    plz = ""
    category = ""
    
    def __init__(self, s,e,p,c, t):
        self.startingpoint = s
        self.endpoint = e
        self.plz = p
        self.category = c
        self.timeframe = t

    #find HelpRequests that fulfill search criteria
    def findRequests(self):
        listRequests = getHelpRequestList()
        potentialMatches : HelpRequest[100]
        for l in listRequests:
            if (l.getActive):
                if(l.getVisible):
                    if(l.getStartingTime > self.startingpoint):
                        if(l.getEndTime < self.endpoint):
                            if(l.category == self.category):
                                if(self.plz == l.getPLZ):
                                    potentialMatches.append(l)

        return potentialMatches