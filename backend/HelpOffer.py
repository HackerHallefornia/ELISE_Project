class HelpOffer():
    comment = ""
    
    def __init__(self, c):
        self.comment = c
    
    def getComment(self):
        return self.comment

    def setComment(self, c):
        self.comment = c