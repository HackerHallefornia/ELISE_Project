from datetime import date
import ListHandling
class User:
    email = ""
    pasword = ""
    vorname = ""
    nachname = ""
    plz = ""
    dob = date(1900,1,1)
    rating = 0.0
    number_ratings = 0
    bio = ""
    username = ""


    def __init__(self,e,pwd,v,n,p,a,d,b,u,ph,st, nr=0, r=0.0):
        self.email = e
        self.password = pwd
        self.vorname = v
        self.nachname = n
        self.plz = p
        self.adress = a
        self.dob = d
        self.bio = b
        self.username = u
        self.phonenumber= ph
        self.status =st
        self.number_rating = nr
        self.rating = r
        

    def to_json(self):
      return {"Username":self.username,
     "Email":self.email, 
     "FirstName":self.vorname, 
     "LastName":self.nachname,
     "Password": self.password ,
     "Birthdate":self.dob,
     "Adress":self.adress,
     "PLZ":self.plz,
     "Phonenumber":self.phonenumber,
     "Rating":self.rating,
     "NumberRatings":self.number_rating,
     "Bio":self.bio ,  
     "Status":self.status}

    def getEmail(self):
        return self.email
    
    def getPassword(self, p):
        return self.password
    
    def loginUser(self, p):
        if self.password == p:
            return True
        else:
            return False
    def sendHelpOffer(self, id):
        if(self.status == "Helper"):
            ListHandling.add_offer_to_request(self.username, id)
    
    def give_rating(self, rating):
        self.rating = ((self.rating* float(self.number_rating) + rating) / float(self.number_rating) +1)
        self.number_rating += 1