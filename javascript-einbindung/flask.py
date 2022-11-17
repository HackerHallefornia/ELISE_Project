from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET', 'POST'])
def login():
    return "True"



@app.route('/login.html', methods=['GET', 'POST'])
def loginReg():

   # if request.method == 'GET':
    return render_template('login.html')



@app.route('/Registrierung_Email_PW.html', methods=['GET', 'POST'])
def emailPw():

    #if request.method == 'GET':
        return render_template('Registrierung_Email_PW.html')

"""
    if request.method == 'POST':
        emailReg = request.form.get('email')
        passwordReg = request.form.get('password')
        return render_template('Registrierung_Name.html')

"""


@app.route('/Registrierung_Name.html', methods=['GET', 'POST'])
def name():


    #if request.method == 'GET':
        return render_template('Registrierung_Name.html')
"""
    if request.method == 'POST':
        vornameReg = request.form.get('vorname')
        nachnameReg = request.form.get('nachname')
        #return render_template('Registrierung_PLZ.html')

"""

@app.route('/Registrierung_PLZ.html', methods=['GET', 'POST'])
def plz():


    #if request.method == 'GET':
        return render_template('Registrierung_PLZ.html')
"""
    if request.method == 'POST':
        plz = request.form.get('plz')
        return render_template('Registrierung_Geburtsdatum.html')
"""

@app.route('/Registrierung_Geburtsdatum.html', methods=['GET', 'POST'])
def geburtsdatum():

    #if request.method == 'GET':
         return render_template('Registrierung_Geburtsdatum.html')
"""
    if request.method == 'POST':
        dateOfBirth = request.form.get('geburtsdatum')
        return render_template('Registrierung_Zusammenfassung.html')
"""





@app.route('/Registrierung_Zusammenfassung.html', methods=['GET', 'POST'])
def zsmfssg():

        return render_template('Registrierung_Zusammenfassung.html')

        if request.method == 'POST':
            email = request.form.get('email')
            return render_template('login.html', Email = email)

"""
@app.route('/server', methods=['POST'])
def server():

    return json.dumps({'success':True}), 200, {'ContentType':'application/json'}



    #hier später get funktion aus Json
"""




