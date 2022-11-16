from flask import Flask, render_template, request, jsonify
import ListHandling

app = Flask(__name__)

@app.route('/')
def hello():
    return "Main Page"


@app.route('/test', methods=['GET', 'POST'])
def test():    # GET request
    if request.method == 'GET':
        return render_template('test.html') 
    
    if request.method == 'POST':
        return request.form.get('testVariable')
    
@app.route('/register', methods=['GET', 'POST'])
def registerRouting():
    if request.method == 'POST':
        return render_template('register.html')
    if request.method == 'GET': #todo change get request variables
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
        ListHandling.register(mail, password, vorname, nachname,plz, adress, dateOfBirth, rating, info, username, telefonnummer, status) 
        return render_template() #todo: insert html file

@app.route('/login', methods=['GET', 'POST']) # POST request login page
def loginRouting():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        login_success = ListHandling.login(email, password)
        if login_success:
            return "Login Successful" #todo: redirect to main page
        else:
            return render_template('login.html', error="Invalid Credentials") #todo: remove ERROR MESSAGE?

@app.route('/requestHelp', methods=['GET', 'POST'])
def requestHelp():
    if request.method == 'GET':
        return render_template('requestHelp.html')
    if request.method == 'POST':
        username = request.form.get('username')
        #todo: get all other variables
        #todo: call backend function
        return render_template('') #todo: insert html file

@app.route('/offerHelp', methods=['GET', 'POST'])
def offerHelp():
    if request.method == 'GET':
        return render_template('offerHelp.html')
    if request.method == 'POST':
        username = request.form.get('username')
        return render_template('') #todo: insert html file
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)