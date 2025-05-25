import flask
from flask import request
import time
import os
from data import *

#Creating the application server
app = flask.Flask(__name__)

#Creating major variables
cred = read_cred()
companies = read_companies()
requests = buy_requests()
sell_request = sell_requests()
user = ""
admin_ = False      #Flag for admin login

#Home page
@app.route("/")
def home():
    return flask.render_template("home.html")

#Login page
@app.route("/login")
def login():
    return flask.render_template("login.html")

@app.route("/login_chk", methods=["POST"])
def login_chk():
    global user
    global companies
    global requests
    global admin_
    user = request.form.get("uname")
    pswd = request.form.get("password")
    
    if cred.get(user) == None or cred[user] != pswd:        #Incorrect username/password
        return flask.render_template("sorry.html")
    
    elif user == "admin":                               #Admin login
        admin_ = True
        return flask.redirect("http://127.0.0.1:5000/admin")
    
    else:                                               #Normal login
        return flask.redirect("http://127.0.0.1:5000/dashboard")

#Signup page
@app.route("/signup")
def signup():
    return flask.render_template("signup.html")

@app.route("/create_acc", methods=["POST"])
def create_acc():
    uname = request.form.get("uname")
    pswd = request.form.get("password")
    
    #Storing new usernames in file
    u = open("Usernames.txt","a+")
    u.write(str(uname)+","+str(pswd)+"\n")
    u.close()
    global cred 
    cred = read_cred()
    return flask.render_template("congrats.html")

#Admin dashboard
@app.route("/admin", methods=["GET","POST"])
def admin():
    global requests
    global admin_
    global companies
    requests = buy_requests()
    companies = read_companies()
    if admin_ == True:
        print("2",requests)
        return flask.render_template("admin.html", requests=requests,companies=companies)
    else:
        return flask.render_template("admin_no.html") #Making sure users dont access admin page

#Buy requests page
@app.route("/admin_buy")
def admin_buy():
    global requests
    requests = buy_requests()
    return flask.render_template("admin_buy.html",requests=requests)

#Sell requests page
@app.route("/admin_sell")
def admin_sell():
    global sell_request
    sell_request = sell_requests()
    return flask.render_template("admin_sell.html",requests=sell_request)

#Active users
@app.route("/users")
def users():
    global cred 
    users = cred.keys()
    return flask.render_template("users.html",users=users)

#Buy page
@app.route("/dashboard", methods=["GET","POST"])
def dashboard():
    global companies
    companies = read_companies()
    
    if admin_ == False and user != "":
        return flask.render_template("dashboard.html", requests=requests,companies=companies)
    else:
        return flask.render_template("admin_no.html")
    
    return flask.render_template("dashboard.html", companies=companies, img="\static\main_logo.jpg")

@app.route("/buy_page")
def buy_page():
    global companies
    companies = read_companies()
    return flask.render_template("buy_page.html", companies=[i[0] for i in companies])

#Store their stock request in file
@app.route("/store", methods=["POST"])
def store():
    global user
    comp_name = request.form.get("cname") 
    quantity = request.form.get("quantity")  
    buy = open("BuyRequests.txt","a+")
    buy.write(str(user)+","+str(comp_name)+","+str(quantity)+"\n")
    buy.close()
    return flask.render_template("thanks.html", message=user.capitalize()+" your request has been submitted successfully and the same will be conveyed to our admin. Our representatives will get in touch with you soon.") 

#Sell page
@app.route("/sell_page")
def sell():
    global companies
    companies = read_companies()
    return flask.render_template("sell_page.html", companies=[i[0] for i in companies])

#Store their stock request in file
@app.route("/store_sell", methods=["POST"])
def store_sell():
    global user
    comp_name = request.form.get("cname") 
    quantity = request.form.get("quantity")  
    sell = open("SellRequests.txt","a+")
    sell.write(str(user)+","+str(comp_name)+","+str(quantity)+"\n")
    sell.close()
    return flask.render_template("thanks.html", message=user.capitalize()+" your request has been submitted successfully and the same will be conveyed to our admin. Our representatives will get in touch with you soon.") 


@app.route("/<company>")
def company(company):
    return flask.render_template("{}.html".format(company))

#Running and executing the application
app.run()