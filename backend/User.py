from datetime import date
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


    def __init__(self,e,pwd,v,n,p,a,d,r,b,u,ph,st):
        self.email = e
        self.password = pwd
        self.vorname = v
        self.nachname = n
        self.plz = p
        self.adress = a
        self.dob = d
        self.rating = r
        self.bio = b
        self.username = u
        self.number_rating = 0
        self.phonenumber= ph
        self.status =st

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
     "Status":"Helper"}

    def getEmail(self, e):
        return self.email
    
    def getPassword(self, p):
        return self.password
    
    def loginUser(self, p):
        if self.password == p:
            return True
        else:
            return False
