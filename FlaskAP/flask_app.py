from flask import Flask, render_template, request, jsonify,redirect, url_for, session
import backend.ListHandling as ListHandling
app = Flask(__name__)

app.secret_key = "JohannesGoebelIstBlöd"

@app.route("/home")
def startpage():
    value = session["username"]
    return render_template('ServiceBereich.html', ownUserName= value)


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
          passwordReg = request.form["passwordReg"]
          passwordRep = request.form["passwordRep"]

          if (passwordReg == passwordRep) and (email!= ""):
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
          session["plz"]= plz
          if plz!="":

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
          session["geburtsdatum"]= geburtsdatum
          if geburtsdatum!="":

                return redirect(url_for("zsmfssg"))
        else:
            pass

    else:
       return render_template('Registrierung_Geburtsdatum.html')





@app.route('/Registrierung_Zusammenfassung', methods=['GET', 'POST'])
def zsmfssg():

    if request.method == 'GET':
        email = session["email"]
        vorname = session["vorname"]
        nachname = session["nachname"]
        plz = session["plz"]
        geburtsdatum = session["geburtsdatum"]
        return render_template('Registrierung_Zusammenfassung.html'
        , Email = email
        , Vorname = vorname
        , Nachname = nachname
        , Postleitzahl = plz
        , Geburtsdatum = geburtsdatum)

    if request.method == 'POST':

        if request.form.get('end') == 'Daten senden':
            # pwd= session["]
            # ListHandling.register(email,

            #     )
            return render_template('ServiceBereich.html')
        else:
            pass

    else:
       return render_template('Registrierung_Zusammenfassung.html')




#session speichern für userdaten



"""
@app.route('/server', methods=['POST'])
def server():

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}



    #hier später get funktion aus Json
"""




