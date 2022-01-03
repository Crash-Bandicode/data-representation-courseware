from flask import Flask, url_for, request, redirect, abort

app = Flask(__name__, static_url_path='', static_folder='static_pages')

@app.route('/')
def index():
    return redirect (url_for('login'))

@app.route('/login')
def login():
    return abort(401)
    return "served by login"

@app.route('/user')
def getUser():
    return "servedby getUser"

@app.route('/user', methods=['POST'])
def createUser():
    return "servedby createUser"

@app.route('/user/<int:id>')
def findByIDUser(id):
    return "Served by findByIDUser with id = "+str(id)

@app.route("/demo_url_for")
def demoUrlFor():
    returnString = "url For index is "+url_for('index')
    returnString += "<br/>"
    returnString += "url for findByIDUser "+ url_for('findByIDUser', id=12)
    return returnString

@app.route('/demo_request', methods=['POST', 'GET', 'DELETE'])
def demoRequest():
    return request.method



if __name__ == "__main__":
    print("in if")
    app.run(debug=True)

