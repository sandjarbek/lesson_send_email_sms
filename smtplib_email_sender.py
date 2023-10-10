import smtplib
import os

sender = "sanjarbek.soatov1989@gmail.com"
receiver = "sanjarbek.89.ss@gmail.com"
# password = os.getenv("PASSWORD")
password = "wkhiaexeauqdlhlb"

message = """
Subject: Hello Hello
This is Ardit!
Just wanted to say hello!
"""

server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)

server.login(sender, password)
server.sendmail(sender, receiver, message)