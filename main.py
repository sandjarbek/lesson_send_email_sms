import yagmail
import os
import time
from _datetime import datetime as dt

sender = "sanjarbek.soatov1989@gmail.com"
reseiver = "sanjarbek.89.ss@gmail.com"


subject = "This is the subject"

contents = """This is the content of the email"""

yag = yagmail.SMTP(user=sender, password=os.getenv("PASSWORD"))

while True:
    now = dt.now()
    if now.hour ==17 and now.minute ==41:
        yag.send(to=reseiver, subject=subject, contents=contents)
        print("Email Send")
        time.sleep(60)