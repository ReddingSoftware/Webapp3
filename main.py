from flask import Flask, session,request,redirect
from daBaseHandler import *


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


class Test(BaseHandler):
    def get(self):
        self.response.write("Test Page Get")
    def post(self):
        self.response.write("Test Page Post")

#Example of session The session is converted to a Flask session
class MainPage(BaseHandler):
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


#Here you'll change your old webapp2 handler to a Flask handler        
@app.route('/',methods=['GET','POST'])    
def MainDef():
    if request.method == 'GET':    
        darequests=request.form
        #you'll your webapp2 class name here in each handler
        daPage= MainPage()
        daPage.request=darequests
        daPage.get()
        if daPage.ChangePage=="None":
            return daPage.data
        else:
            return redirect(daPage.ChangePage)
    if request.method == 'POST':
        darequests=request.form
        daPage= MainPage()
        daPage.request=darequests
        daPage.post()
        if daPage.ChangePage=="None":
            return daPage.data
        else:
            return redirect(daPage.ChangePage)

@app.route('/FirstPage',methods=['GET','POST'])    
def FirstDef():
    if request.method == 'GET':    
        darequests=request.form
        daPage= FirstPage()
        daPage.request=darequests
        daPage.get()
        if daPage.ChangePage=="None":
            return daPage.data
        else:
            return redirect(daPage.ChangePage)
    if request.method == 'POST':
        darequests=request.form
        daPage= FirstPage()
        daPage.request=darequests
        daPage.post()
        if daPage.ChangePage=="None":
            return daPage.data
        else:
            return redirect(daPage.ChangePage)

@app.route('/SecondPage',methods=['GET','POST'])    
def SecondDef():
    if request.method == 'GET':    
        darequests=request.form
        daPage= SecondPage()
        daPage.request=darequests
        daPage.get()
        if daPage.ChangePage=="None":
            return daPage.data
        else:
            return redirect(daPage.ChangePage)
    if request.method == 'POST':
        darequests=request.form
        daPage= SecondPage()
        daPage.request=darequests
        daPage.post()
        if daPage.ChangePage=="None":
            return daPage.data
        else:
            return redirect(daPage.ChangePage)

@app.route('/test',methods=['GET','POST'])    
def TestDef():
    if request.method == 'GET':    
        darequests=request.form
        daPage= Test()
        daPage.request=darequests
        daPage.get()
        if daPage.ChangePage=="None":
            return daPage.data
        else:
            return redirect(daPage.ChangePage)
    if request.method == 'POST':
        darequests=request.form
        daPage= Test()
        daPage.request=darequests
        daPage.post()
        if daPage.ChangePage=="None":
            return daPage.data
        else:
            return redirect(daPage.ChangePage)

