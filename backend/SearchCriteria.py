from datetime import datetime


class SearchCriteria():
    startingpoint = datetime(1900,1,1,12,0)
    endpoint = datetime(1900,1,1,12,0)
    timeframe = False
    plz = ""
    categories = ""
    
    def __init__(self,u, s,e,p,c, t):
        self.username = u
        self.startingpoint = s
        self.endpoint = e
        self.plz = p
        self.categories = c
        self.timeframe = t


    
    