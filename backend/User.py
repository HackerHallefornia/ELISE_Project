from datetime import date
import ListHandling
import Utilities

class User:
    email = ""
    pasword = ""
    vorname = ""
    nachname = ""
    plz = ""
    dob = date(1900,1,1)
    rating = 0.0
    number_rating = 0
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
    
    def give_rating(self, new_rating):
            self.rating = compute_new_rating(self.number_rating, self.rating, new_rating)
            self.number_rating = int(self.number_rating) + 1
            user_list = Utilities.getUserlist()
            Utilities.updateUserInUserlist(user_list, self)
            # update User in Userlist

def compute_new_rating(num_rating, avg_rating, r):
    total = avg_rating * num_rating
    new_total = total + r
    new_avg = new_total / (num_rating + 1)
    return round (new_avg, 2)