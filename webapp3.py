from flask import Flask, session,request,redirect, url_for
import io
import os
import requests
MailConFigExists=False
try:
  from MailConfigFile import *
  MailConFigExists=True
except:
  try:
    from main import MailConfig
    MailConFigExists=True
  except:
    pass


app = Flask(__name__)



def webapp(arg):
  if request.method == 'GET':    
      return webappGet(arg)
  if request.method == 'POST':
      return webappPost(arg)

class Response:
  def __init__(self, handler):
    self.handler = handler

  def write(self, stuffAdd):
    self.handler.data += stuffAdd

class ReqFile:
  def get(self,arg):
    file = request.files[arg]
    return file

class DaRequest:
  def __init__(self):
    self.remote_addr = request.remote_addr
    self.POST = ReqFile()

  def get(self,arg):
    return request.form.get(arg)

  

class BaseHandler:
  
  def __init__(self):
    self.data = ""
    self.ChangePage="None"
    self.response = Response(self)
    self.session = session
    self.request= DaRequest()
  def redirect(self,arg):
    self.ChangePage=arg

class RequestHandler(BaseHandler):
  pass



def webappGet(daPage):
    daPage.get()
    if daPage.ChangePage=="None":
        return daPage.data
    else:
        return redirect(daPage.ChangePage)

def webappGetRequest(daPage,path):
    daPage.get(path)
    if daPage.ChangePage=="None":
        return daPage.data
    else:
        return redirect(daPage.ChangePage)

def webappPost(daPage):
    daPage.post()
    if daPage.ChangePage=="None":
        return daPage.data
    else:
        return redirect(daPage.ChangePage)

class webapp2():
  RequestHandler = RequestHandler
  def WSGIApplication(dislist,searchURL):
    dasearchURL="/"+searchURL
    a=0
    while a < len(dislist):
        if dislist[a][0]==dasearchURL:
            daCall= dislist[a][1]
            return daCall
            
        a+=1

if MailConFigExists==True:
  class mail():
    def daMail(url,key,first,last,email,to,subject,text):
      return requests.post(
        url,
        auth=("api", key),
        data={"from": "%s %s <%s>" % (first,last,email),
          "to": [to],
          "subject": subject,
          "text": text})        
    def send_mail(to,subject,body,sender=MailConfig.config.get("Defalt_Sender")):
        AlwaysDefalt=MailConfig.config.get("Always_Use_Defalt_Sender")
        defaultSender=MailConfig.config.get("Defalt_Sender")
        MailKey=MailConfig.config.get("Key")
        URL=MailConfig.config.get("URL")
        First=MailConfig.config.get("First_Name")
        Last=MailConfig.config.get("Last_Name")
        if AlwaysDefalt==True:
          return mail.daMail(URL,MailKey,First,Last,defaultSender,to,subject,body)
        elif sender==defaultSender:
          return mail.daMail(URL,MailKey,First,Last,defaultSender,to,subject,body)
        else:
          return mail.daMail(URL,MailKey,'','',sender,to,subject,body)

