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

    def __init__(self,e,pwd,v,n,p,a,d,r,b,u):
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

    def get_email():
        return email