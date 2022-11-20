from flask import Flask, render_template, request, jsonify,redirect, url_for, session
from backend import ListHandling
from backend import Utilities
from backend.SearchCriteria import SearchCriteria
from datetime import datetime
app = Flask(__name__)

app.secret_key = "4b0dda699e6179fc0125c49ba3116be57145d44f"

@app.route("/Posteingang/<name>", methods= ["POST", "GET"])
def inbox(name):
    #unser username ist email
    if request.method == "GET":
        if "user" in session:
            u = session["user"]
            chat_partner = name
            message_list = ListHandling.get_messages_for_chat(u,chat_partner)
            return render_template("Posteingang.html", sender_name = chat_partner, messages = message_list)
        else: 
            return redirect(url_for("login"))
    if request.method == "POST":

        print("Hello")
        if request.form["Senden"] == "Send":
            content = request.form["content"]
            ListHandling.send_message(session["user"], name, content)
            return redirect(url_for("inbox", name=name))

@app.route("/home", methods=['GET', 'POST'])
def startpage():
    if request.method == 'GET':
        if "username" in session:
            user = session["username"]
            return render_template('ServiceBereich.html', ownUserName= user)
        else:
            return redirect(url_for(loginReg))

    # nicht sicher ob das so stimmt eventuell muss die Post nicht dazu für die Session abfrage
    #TODO Seiten verknüpfen
    if request.method == "POST":
        if request.form.get('vermittlung') == "Vermittlungsliste":
            return "1"
        if request.form.get('hilfsanfrage') == "Hilfsanfrage erstellen":
            return redirect(url_for("offer_help"))
        if request.form.get('hilfsangebot') == "Hilfe anbieten":
            return "3"
        if "username" in session:
            user = session["username"]
            return render_template('ServiceBereich.html', ownUserName= user)
        else:
            return redirect(url_for(loginReg))

@app.route("/")
def home():
    return redirect(url_for("loginReg"))

@app.route('/login.html', methods=['GET', 'POST'])
def loginReg():
   if request.method == 'GET':
         return render_template('login.html')
   if request.method == 'POST':

       if request.form.get('login') == 'Anmelden':
           username = request.form["nutzer"]

           password = request.form["password"]
           Login_var = ListHandling.login(username, password)
           if Login_var[0] == True:

                session["username"]= Login_var[1]
                return redirect(url_for("startpage"))
           else:
                return render_template('login.html')

       elif request.form.get('register') == 'Registrieren':
            return redirect(url_for("register"))
       else:
            pass

   else:
       return render_template('login.html')

@app.route('/Registrierung', methods=['GET', 'POST'])
def register():

    if request.method == 'GET':
        return render_template('Registrierung_Email_PW.html')


    if request.method == 'POST':

        if request.form.get('next') == 'Weiter':
          email = request.form["email"]
          username = request.form["username"]
          passwordReg = request.form["passwordReg"]
          passwordRep = request.form["passwordRep"]

          if (passwordReg == passwordRep) and (email!= ""):
              session["username"]= username
              session["password"]= passwordReg
              session["email"]= email
              return redirect(url_for("name"))
          else:
              return render_template('Registrierung_Email_PW.html')
        else:
            pass

    else:
       return render_template('Registrierung_Email_PW.html')

@app.route('/Registrierung_Name', methods=['GET', 'POST'])
def name():

    if request.method == 'GET':
        return render_template('Registrierung_Name.html')


    if request.method == 'POST':

        if request.form.get('next') == 'Weiter':
          vorname = request.form["vorname"]
          nachname = request.form["nachname"]
          if (vorname!="") or (nachname!=""):
            session["vorname"]= vorname
            session["nachname"]= nachname
            return redirect(url_for("plz"))
        else:
            pass

    else:
       return render_template('Registrierung_Name.html')

@app.route('/Registrierung_PLZ', methods=['GET', 'POST'])
def plz():


    if request.method == 'GET':
        return render_template('Registrierung_PLZ.html')

    if request.method == 'POST':

        if request.form.get('next') == 'Weiter':
          plz = request.form["plz"]

          if plz!="":
            session["plz"]= plz
            return redirect(url_for("geburtsdatum"))
        else:
            pass

    else:
       return render_template('Registrierung_PLZ.html')

@app.route('/Registrierung_Geburtsdatum', methods=['GET', 'POST'])
def geburtsdatum():

    if request.method == 'GET':
        return render_template('Registrierung_Geburtsdatum.html')

    if request.method == 'POST':

        if request.form.get('next') == 'Weiter':
          geburtsdatum = request.form["geburtsdatum"]

          if geburtsdatum!="":
            session["geburtsdatum"]= geburtsdatum
            return redirect(url_for("zsmfssg"))
        else:
            pass

    else:
       return render_template('Registrierung_Geburtsdatum.html')

@app.route('/Registrierung_Zusammenfassung', methods=['GET', 'POST'])
def zsmfssg():

    if request.method == 'GET':
        email = session["email"]
        username = session["username"]
        vorname = session["vorname"]
        nachname = session["nachname"]
        plz = session["plz"]
        geburtsdatum = session["geburtsdatum"]
        return render_template('Registrierung_Zusammenfassung.html'
        , Email = email
        , Username = username
        , Vorname = vorname
        , Nachname = nachname
        , Postleitzahl = plz
        , Geburtsdatum = geburtsdatum)

    if request.method == 'POST':

        if request.form.get('end') == 'Daten senden':
            pwd= session["password"]
            email = session["email"]
            username = session["username"]
            vorname = session["vorname"]
            nachname = session["nachname"]
            plz = session["plz"]
            geburtsdatum = session["geburtsdatum"]

            ListHandling.register(email,pwd,vorname,nachname,plz,geburtsdatum, username)

            return redirect(url_for("startpage"))#render_template('ServiceBereich.html')
        else:
            render_template('Registrierung_Zusammenfassung.html')

    else:
       return render_template('Registrierung_Zusammenfassung.html')


@app.route('/Hilfe_anbieten', methods=['GET', 'POST'])
def offer_help():
    if request.method == 'GET':
        return render_template('Hilfsanbieten_Menu.html')

    if request.method == 'POST':

        mocklist = ["Annemarie", "Peter", "Jonathan"]
        search_object_mock= SearchCriteria("john_doe", datetime(2022,1,1,12,0), datetime(2022,12,20,12,0),"06114","social",True)

        if request.form.get('submit_search') == 'suchen':
            # EIntragen von Suchkriterien
            startdate = datetime.strptime(request.form['startdate'],'%Y-%m-%d')
            enddate = datetime.strptime(request.form['enddate'],'%Y-%m-%d')
            plz = request.form['zipcode']
            cat = Utilities.html_category_import(request.form['category'])
            search_object = SearchCriteria("john_doe", startdate, enddate, plz, cat, True)
            fitting_helpseekers_list = ListHandling.get_filtered_help_request_list(search_object)
            format_name_for_display = [fitting_helpseekers_list[0].username]
            return render_template('Hilfsanbieten_Menu.html', Helpseekers=format_name_for_display)
        if request.form.get('submit_antrag') != '':
            to_print = request.form.get('submit_antrag')
            return to_print

@app.route('/Hilfsgesuch_erstellen', methods=['GET', 'POST'])       
def hilfe():

     if request.method == 'GET':

        return render_template('Kategorie.html')

     if request.method == 'POST':   

        if request.form.get('Auswahl') == 'Hilfe beim Einkauf':
            session["Kategorie"]= "Hilfe beim Einkauf"
            return redirect(url_for("taguhrzeit"))

        if request.form.get('Auswahl') == 'Hilfe beim Transport':
            session["Kategorie"]= "Hilfe beim Transport"
            return redirect(url_for("taguhrzeit"))

        if request.form.get('Auswahl') == 'Unterstützung im Haushalt':
            session["Kategorie"]= "Unterstützung im Haushalt"
            return redirect(url_for("taguhrzeit"))

        if request.form.get('Auswahl') == 'Begleitung zum Termin':
            session["Kategorie"]= "Begleitung zum Termin"
            return redirect(url_for("taguhrzeit"))

        if request.form.get('Auswahl') == 'Hilfe mit dem Haustier':
            session["Kategorie"]= "Hilfe mit dem Haustier"
            return redirect(url_for("taguhrzeit"))

        if request.form.get('Auswahl') == 'Technische Probleme':
            session["Kategorie"]= "Technische Probleme"           
            return redirect(url_for("taguhrzeit"))

        if request.form.get('Auswahl') == 'Soziales und Kultur':
            session["Kategorie"]= "Soziales und Kultur"
            return redirect(url_for("taguhrzeit"))

        if request.form.get('Auswahl') == 'Handwerkliche Hilfe':
            session["Kategorie"]= "Handwerkliche Hilfe"
            return redirect(url_for("taguhrzeit"))

        if request.form.get('Auswahl') == 'Bürokratie':
            session["Kategorie"]= "Bürokratie"             
            return redirect(url_for("taguhrzeit"))
   

@app.route('/TagUhrzeit', methods=['GET', 'POST'])       
def taguhrzeit():

    if request.method == 'GET':
        return render_template("Tag_Uhrzeit.html")

    if request.method == 'POST':

        if request.form.get('next') == 'Weiter':
          date = request.form["date"]
          time = request.form["time"]
          if (date!="") or (time!=""):
            session["date"]= date
            session["time"]= time
            return redirect(url_for("treffpunkt"))

@app.route('/Treffpunkt', methods=['GET', 'POST'])       
def treffpunkt():

    if request.method == 'GET':
        return render_template("Treffpunkt.html")

    if request.method == 'POST':

        if request.form.get('next') == 'Weiter':
          treffpunkt = request.form["plz"]
          if (treffpunkt!="") :
            session["treffpunkt"]= treffpunkt
            return redirect(url_for("uebersicht"))

@app.route('/Übersicht', methods=['GET', 'POST'])       
def uebersicht():

    if request.method == 'GET':
        kategorie = session["Kategorie"]
        date = session["date"]
        time = session["time"]
        treffpunkt = session["treffpunkt"]
        return render_template("Übersicht.html"
        , Kategorie = kategorie
        , Date = date
        , Time = time
        , Treffpunkt = treffpunkt)

if __name__ == "__main__":
    app.run(debug=True)


