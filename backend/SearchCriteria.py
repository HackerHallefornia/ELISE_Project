from datetime import datetime
class SearchCriteria():
    startingpoint = datetime(1900,1,1,12,0)
    endpoint = datetime(1900,1,1,12,0)
    plz = ""
    category = ""
    def __init__(self, s,e,p,c):
        self.startingpoint = s
        self.endpoint = e
        self.plz = p
        self.category = c
