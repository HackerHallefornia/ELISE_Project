from flask import Flask

app = Flask(__name__)

@app.route("/")

def index():
    return "Hello this is the new version!"


def listOfHelpers(time, place, category):
    return 0
def listOfTasks(time, place, category):
    return 0

app.run(host='0.0.0.0', port=81)