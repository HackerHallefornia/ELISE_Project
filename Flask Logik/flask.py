from flask import Flask, render_template, request, jsonify,redirect, url_for, session

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

   if request.method == 'POST':

       if request.form.get('login') == 'Anmelden':
           username = request.form["nutzer"]
           password = request.form["password"]
           session["username"]= username
           if username != "":
       # logik einloggen
                return redirect(url_for("startpage"))

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

"""
    if request.method == 'POST':
        emailReg = request.form.get('email')
        passwordReg = request.form.get('password')
        return render_template('Registrierung_Name.html')

"""


@app.route('/Registrierung_Name', methods=['GET', 'POST'])
def name():


    #if request.method == 'GET':
        return render_template('Registrierung_Name.html')
"""
    if request.method == 'POST':
        vornameReg = request.form.get('vorname')
        nachnameReg = request.form.get('nachname')
        #return render_template('Registrierung_PLZ.html')

"""

@app.route('/Registrierung_PLZ', methods=['GET', 'POST'])
def plz():


    #if request.method == 'GET':
        return render_template('Registrierung_PLZ.html')
"""
    if request.method == 'POST':
        plz = request.form.get('plz')
        return render_template('Registrierung_Geburtsdatum.html')
"""

@app.route('/Registrierung_Geburtsdatum', methods=['GET', 'POST'])
def geburtsdatum():

    #if request.method == 'GET':
         return render_template('Registrierung_Geburtsdatum.html')
"""
    if request.method == 'POST':
        dateOfBirth = request.form.get('geburtsdatum')
        return render_template('Registrierung_Zusammenfassung.html')
"""





@app.route('/Registrierung_Zusammenfassung', methods=['GET', 'POST'])
def zsmfssg():

        return render_template('Registrierung_Zusammenfassung.html')

        if request.method == 'POST':
            email = request.form.get('email')
            return render_template('login.html', Email = email)





#session speichern für userdaten



"""
@app.route('/server', methods=['POST'])
def server():

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}



    #hier später get funktion aus Json
"""




