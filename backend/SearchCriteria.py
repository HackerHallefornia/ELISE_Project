from datetime import datetime

class SearchCriteria():
    startingpoint = datetime(1900,1,1,12,0)
    endpoint = datetime(1900,1,1,12,0)
    timeframe = False
    plz = []
    categories = []
    
    def __init__(self,u, s,e,p,c, t):
        self.username = u
        self.startingpoint = s
        self.endpoint = e
        self.plz = p
        self.categories = c
        self.timeframe = t
        
    
    def to_json(self):
      return {"Username":self.username, 
            "categories":",".join(self.categories), 
            "PLZ":",".join(self.categories),
            "time_start":self.startingpoint,
            "time_end":self.endpoint,
            "timeframe":self.timeframe}


    def compare_to_help_request(self, help_request):
        if self.username == help_request.username:
            if help_request.plz in self.plz:
                if self.categories == help_request.categories:
                    if self.startingpoint > help_request.startingpoint:
                        if help_request.timeframe == True:
                            if help_request.endpoint < self.endpoint:
                                return True
                        else:
                            if help_request.startingpoint < self.endpoint:
                                return True