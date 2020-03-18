#This file is just an example file to demonstrate how the webapp3-flask module works

from flask import Flask, session,request,redirect
"""
If you want to use the mail feature to convert the google mail syntax to work for mailgun you need to either 
add this class before you import webapp3 or put this class in a python file and name it MailConfigFile.py and import the file 
BEFORE you import webapp3
class MailConfig():
    config={"Key":"your-Mailgun-Key","Defalt_Sender":"YOU@YOUR_DOMAIN_NAME","Always_Use_Defalt_Sender":True,"URL":"https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages","First_Name":"Default First Name","Last_Name":"Default Last Name"}
"""
from MailConfigFile import MailConfig
from webapp3 import *
#or you can use
#from webapp3 import BaseHandler,webapp2,RequestHandler,webappGet,webappPost

#Make sure to pip install it first using
#pip3 install webapp3-flask 
#also we recommend that you install it using your requirements.txt


#make sure to add this
app = Flask(__name__)

#start Examples of webapp2 classes

#Example redirect
class FirstPage(BaseHandler):
    def get(self):
        self.redirect("/SecondPage")
    def post(self):
        self.response.write("First Page Post")

class SecondPage(BaseHandler):
    def get(self):
        self.response.write("second page")
    def post(self):
        self.response.write("Second Page Post")


class Test(webapp2.RequestHandler):
    def get(self):
        self.response.write("Test Page Get")
    def post(self):
        self.response.write("Test Page Post")

#Example of session The session is converted to a Flask session
class MainPage(webapp2.RequestHandler):
    def get(self):  
        self.session["name"]="Some Name"
        self.session["phone"]="8675309"
        self.response.write("""
        <html>
        <head>
        </head>
        <body>
        """)
        self.response.write("first thing to add")
        self.response.write("""
        <form method="post" action="/">
            <input type="text" name="name">
            <input type="submit">
        """)
        self.response.write("""
        </body>
        </html>
        """)

    def post(self):
        name=self.request.get('name')
        self.response.write("""
        <html>
        <head>
        </head>
        <body>
        """)
        self.response.write("this is the new post page<br/><br/>I posted " + name)
        SessionName=self.session.get("name")
        SessionPhone=self.session.get("phone")
        self.response.write("<br/><br/>my session name is " + SessionName)
        self.response.write("<br/><br/>my session phone number is " + SessionPhone)
        self.response.write("""
        </body>
        </html>
        """)
        
#End Examples of webapp2 classes
     
    
#make sure to set your secret key for Flask
app.secret_key = 'your-secret-key'

#your main page has to be handled individually
@app.route('/',methods=['GET','POST'])    
def MainDef():
    return webapp(MainPage())
#Here you can change your old webapp2 handler to a Flask handler. Make sure to remove your main page
@app.route('/<searchURL>',methods=['GET','POST'])    
def RouteDef(searchURL):    
    app = webapp2.WSGIApplication([
    ('/FirstPage', FirstPage),
    ('/SecondPage', SecondPage),
    ('/test', Test),
    ]
    , searchURL=searchURL ) #when you paste in your old webapp2 handler make sure to remove 
    return webapp(app())    #config, debug, ect. and add searchURL=searchURL
"""
You can handle pages individually like this as well

@app.route('/FirstPage',methods=['GET','POST'])    
def FirstDef():
    if request.method == 'GET':    
        daPage= FirstPage()
        return webappGet(daPage)

    if request.method == 'POST':
        daPage= FirstPage()
        return webappPost(daPage)

@app.route('/SecondPage',methods=['GET','POST'])    
def SecondDef():
    if request.method == 'GET':    
        daPage= SecondPage()
        return webappGet(daPage)
    if request.method == 'POST':
        daPage= SecondPage()
        return webappPost(daPage)

@app.route('/test',methods=['GET','POST'])    
def TestDef():
    if request.method == 'GET':    
        daPage= Test()
        return webappGet(daPage)
    if request.method == 'POST':
        daPage= Test()
        return webappPost(daPage)"""

