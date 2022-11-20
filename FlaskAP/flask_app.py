from flask import Flask, render_template, request, jsonify,redirect, url_for, session
from backend import ListHandling
app = Flask(__name__)

app.secret_key = "4b0dda699e6179fc0125c49ba3116be57145d44f"


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

           if ListHandling.login(username, password) == True:
                session["username"]= username
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

        if request.form.get('submit_search') == 'suchen':
            return render_template('Hilfsanbieten_Menu.html', Helpseekers=mocklist)

        # EIntragen von Suchkriterien

        # passende einträge von der JSON ziehen

        # diese auf der Seite anzeigen


if __name__ == "__main__":
    app.run(debug=True)


