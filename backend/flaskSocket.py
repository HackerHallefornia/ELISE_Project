from flask import Flask, render_template, request, jsonify
import ListHandling

app = Flask(__name__)
    
@app.route('/register', methods=['GET', 'POST'])
def registerRouting():
    if request.method == 'GET':
        return render_template('register.html')
    if request.method == 'POST': #todo change get request variables
        mail = request.form.get('mail')
        password = request.form.get('password')
        vorname = request.form.get('vorname')
        nachname = request.form.get('nachname')
        plz = request.form.get('plz')
        adress = request.form.get('adress')
        dateOfBirth = request.form.get('geburtsdatum')
        rating = 5 #todo rating anpassen
        info = request.form.get('info')
        username = request.form.get('username')
        telefonnummer = request.form.get('telefonnummer')
        status = 'helper'
        register_success = ListHandling.register(mail, password, vorname, nachname,plz, adress, dateOfBirth, rating, info, username, telefonnummer, status) 
        return register_success

@app.route('/login', methods=['GET', 'POST']) # POST request login page
def loginRouting():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        login_success = ListHandling.login(email, password)
        return login_success

@app.route('/requestHelp', methods=['GET', 'POST'])
def requestHelp():
    if request.method == 'GET':
        return render_template('requestHelp.html')
    if request.method == 'POST':
        username = request.form.get('username')
        #todo: get all other variables
        #todo: call backend function
        return True #todo: insert html file

@app.route('/offerHelp', methods=['GET', 'POST'])
def offerHelp():
    if request.method == 'GET':
        return render_template('offerHelp.html')
    if request.method == 'POST':
        username = request.form.get('username')
        return True #todo: insert html file
 
#isHelpAccepted template
@app.route('/isHelpAccepted', methods=['GET', 'POST'])   
def isHelpAccepted():
    if request.method == 'GET':
        return render_template('acceptHelp.html')
    if request.method == 'POST':
        username = request.form.get('username')
        accepted = request.form.get('accepted')
        return accepted


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)