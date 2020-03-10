from flask import Flask, session,request,redirect, url_for

class Response:
  def __init__(self, handler):
    self.handler = handler

  def write(self, stuffAdd):
    self.handler.data += stuffAdd


#this replaces your webapp2 base handler and makes it so that most of your webapp2 syntax will work and run on 
#Python3 using Flask instead of webapp2. It allows you to do self.response.write("whatever"), sessions, and redirects

class BaseHandler:
  def __init__(self):
    self.data = ""
    self.ChangePage="None"
    self.response = Response(self)
    self.session = session
    self.request= {}
  def redirect(self,arg):
    self.ChangePage=arg



    



