from flask import Flask
import pyrebase
from flask import render_template, request
app = Flask(__name__)

config = {
    "apiKey": "AIzaSyC0aHPkUog1aBvaJjwFeKCqM03Uplb77R0",
    "authDomain": "trying-stuff-c1110.firebaseapp.com",
    "databaseURL": "https://trying-stuff-c1110-default-rtdb.firebaseio.com",
    "projectId": "trying-stuff-c1110",
    "storageBucket": "trying-stuff-c1110.appspot.com",
    "messagingSenderId": "482454491691",
    "appId": "1:482454491691:web:94a1ba49b376538477106e",
    "measurementId": "G-PG1LTWELSX"
}

num = 1
firebase = pyrebase.initialize_app(config)
db = firebase.database()
##add/push something
#db.child("names").push({"name":"Shlatt"})

##updating in firebase
#db.child("names").child("name").update({"name":"boom"})

##removing in firebase
#users = db.child("names").child("name").get()
#print(users.val()) --> since getting .child("name"), users.val gives boom
#print(users.key()) --> "name":"boom", gives us name back

##remove
#users = db.child("names").remove()
#users = db.child("names").child("name").remove()
@app.route('/')
def hello_world():
    return render_template("public/register.html")


@app.route('/index.html', methods=["POST"])
def index():
    global num
    num+=1
    emailnum = "user" + str(num)
    email = request.form['email']
    password = request.form['password']
    check = request.form['check']
    db.child("Users Amount").push({emailnum:email})
    

    return render_template("public/index.html", email=email, password=password, check=check)

@app.route('/dashboard.html')
def dashboard():
    return render_template("public/dashboard.html")

@app.route('/bill.html')
def bill():
    return render_template("public/bill.html")


@app.route('/statements.html')
def statements():
    return render_template("public/statements.html")

@app.route('/pollingloc.html')
def pollingloc():
    return render_template("public/pollingloc.html")

"""
@app.route('/begin', methods=["POST"])
def begin():
    global user
    user+=1
    usernum = "user" + str(user)
    username = request.form['username']
    password = request.form['password']
    db.child("user").push({usernum:username})

    return render_template("begin.html", username=username, password=password)
"""