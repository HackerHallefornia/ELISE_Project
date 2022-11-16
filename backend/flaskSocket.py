from flask import Flask, render_template, request, jsonify
from ListHandling import login

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
    
def register():
    if request.method == 'POST':
        return render_template('register.html')
    if request.method == 'GET':
        vorname = request.form.get('vorname')
        nachname = request.form.get('nachname')
        mail = request.form.get('mail')
        plz = request.form.get('plz')
        geburtsdatum = request.form.get('geburtsdatum')
        telefonnummer = request.form.get('telefonnummer')
        info = request.form.get('info')
        #todo: insert backend call here
        return render_template() #todo: insert html file

@app.route('/login', methods=['GET', 'POST']) # POST request login page
def loginRouting():
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        login_success = login(email, password)
        if login_success:
            return "Login Successful" #todo: redirect to main page
        else:
            return render_template('login.html', error="Invalid Credentials") #todo: remove ERROR MESSAGE?



app.run(host='0.0.0.0', port=80)