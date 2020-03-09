from flask import Flask, session,request,redirect, url_for

class Response:
  def __init__(self, handler):
    self.handler = handler

  def write(self, stuffAdd):
    self.handler.data += stuffAdd



class BaseHandler:
  def __init__(self):
    self.data = ""
    self.ChangePage="None"
    self.response = Response(self)
    self.session = session
    self.request= {}
  def redirect(self,arg):
    self.ChangePage=arg



    



