from flask import Flask, session,request,redirect
from webapp3 import *


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
     
        
app.secret_key = 'your-secret-key'


#Here you'll change your old webapp2 handler to a Flask handler and call either the webappGet function or the webappPost function       
@app.route('/',methods=['GET','POST'])    
def MainDef():
    if request.method == 'GET':    
        daPage= MainPage()
        return webappGet(daPage)

    if request.method == 'POST':
        daPage= MainPage()
        return webappPost(daPage)

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
        return webappPost(daPage)

