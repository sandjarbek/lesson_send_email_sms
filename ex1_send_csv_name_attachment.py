import yagmail
import os
import time
from _datetime import datetime as dt
import pandas

sender = "sanjarbek.soatov1989@gmail.com"



subject = "This is the subject"



yag = yagmail.SMTP(user=sender, password=os.getenv("PASSWORD"))

df = pandas.read_csv("content1.csv")
print(df)

for index, row in df.iterrows():
    contents = [f"""hi {row['name']}This is the content of the emai, aomount of the content - {row['amount']}""", row["filepath"]]
    yag.send(to=row["email"], subject=subject, contents=contents)
    print("send email")
