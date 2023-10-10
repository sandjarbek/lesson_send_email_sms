import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from email.mime.base import MIMEBase
from email import encoders

sender = "sanjarbek.soatov1989@gmail.com"
receiver = "sanjarbek.89.ss@gmail.com"
password = os.getenv("PASSWORD")

message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = "Hello again"



body = """
<h2>Hi there!</h2>
There are only two cats flying today!
"""

mimetext = MIMEText(body, 'html')
message.attach(mimetext)

atachment_path = 'tiger.jpeg'
atachment_file = open(atachment_path, 'rb')
payload = MIMEBase('application', 'octate-stream')
payload.set_payload(atachment_file.read())
encoders.encode_base64(payload)
payload.add_header('Content-Disposition', 'attachment', filename=atachment_path)
message.attach(payload)


server = smtplib.SMTP_SSL('smtp.googlemail.com', 465)

server.login(sender, password)
message_text = message.as_string()
print((message_text))
server.sendmail(sender, receiver, message_text)
server.quit()