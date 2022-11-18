from flask import Flask, render_template, request, jsonify
import ListHandling
import SearchCriteria
app = Flask(__name__)

#registration ready
@app.route('/server/register', methods=['GET', 'POST'])
def registerRouting():
    if request.method == 'GET':
        return True
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
        ListHandling.register(mail, password, vorname, nachname,plz, adress, dateOfBirth, rating, info, username, telefonnummer, status) 
        return True
    
#login ready
@app.route('/server/login', methods=['GET', 'POST'])
def loginRouting():
    if request.method == 'GET':
        return True
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        login_success = ListHandling.login(email, password)
        return login_success

#help request  
@app.route('/server/requestHelp', methods=['GET', 'POST'])
def requestHelpRouting():
    if request.method == 'GET':
        return True
    if request.method == 'POST':
        username = request.form.get('username')
        #todo: get all other variables
        #todo: call backend request help
        
        return True
    
#help offer ready
@app.route('/server/offerHelp', methods=['GET', 'POST'])
def offerHelpRouting():
    if request.method == 'GET':
        return True
    if request.method == 'POST':
        user_id = request.form.get('user_id')
        request_id = request.form.get('request_id')
        ListHandling.add_offer_to_request(user_id, request_id)
        return True


#isHelpAccepted template ready
@app.route('/server/isHelpAccepted', methods=['GET', 'POST'])   
def isHelpAccepted():
    if request.method == 'GET':
        return True
    if request.method == 'POST':
        username = request.form.get('username')
        requestId = request.form.get('requestId')
        ListHandling.match(requestId, username)
        return True
        
#give rating ready
@app.route('/server/giveRating', methods=['GET', 'POST'])
def give_ratingRouting():
    if request.method == 'GET':
        return True
    if request.method == 'POST':
        username = request.form.get('username')
        rating = request.form.get('rating')
        ListHandling.give_rating(username, rating)
        return True

#show request list
@app.route('/server/showRequestList', methods=['GET', 'POST'])
def show_request_listRouting():
    if request.method == 'GET':
        return True
    if request.method == 'POST':
        username = request.form.get('username')
        startingpoint = request.form.get('startingpoint')
        endpoint = request.form.get('endpoint')
        plz = request.form.get('plz')
        categories = request.form.get('categories')
        timeframe = request.form.get('timeframe')
        
        searchCriteria = SearchCriteria #todo
        request_list = ListHandling.get_filtered_help_request_list(searchCriteria)
        return True #todo list transfer to html file
        
#show offer list
@app.route('/server/showOfferList', methods=['GET', 'POST'])
def show_offer_listRouting():
    if request.method == 'GET':
        return True
    if request.method == 'POST':
        username = request.form.get('username')
        #todo backend call
        return True
        


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)