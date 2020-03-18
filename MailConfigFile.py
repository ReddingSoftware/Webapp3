
"""
If you want to use the mail feature to convert the google mail syntax to work for mailgun you need to either 
add this class before you import webapp3 or put this class in a python file and name it MailConfigFile.py and import the file 
BEFORE you import webapp3"""

class MailConfig():
    config={"Key":"your-Mailgun-Key","Defalt_Sender":"YOU@YOUR_DOMAIN_NAME","Always_Use_Defalt_Sender":True,"URL":"https://api.mailgun.net/v3/YOUR_DOMAIN_NAME/messages","First_Name":"Default First Name","Last_Name":"Default Last Name"}
