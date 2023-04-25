import smtplib, ssl
from decouple import config
import certifi

port = 465  # For SSL
password = config("APP_KEY")

# Create a secure SSL context
context = ssl.create_default_context(cafile=certifi.where())

mailTo = "rahulnixonbit@gmail.com"
mess = "hello!! how are you?"

message = """From: From {} <{}>
To: To {} <{}>
MIME-Version: 1.0
Content-type: text/html
Subject: SMTP HTML e-mail test

{}
""".format("rahulprojecthotel@gmail.com".split("@")[0], "rahulprojecthotel@gmail.com", mailTo.split("@")[0], mailTo,
           mess)

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login("rahulprojecthotel@gmail.com", password)
    server.sendmail("rahulprojecthotel@gmail.com", mailTo, message)

# sendmail("rahulnixonbit@gmail.com", "hello!! how are you?")
