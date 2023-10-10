import yagmail
import os
import time
from _datetime import datetime as dt
import pandas

sender = "sanjarbek.soatov1989@gmail.com"



subject = "This is the subject"



yag = yagmail.SMTP(user=sender, password=os.getenv("PASSWORD"))

df = pandas.read_csv("contents.csv")
print(df)

for index, row in df.iterrows():
    contents = [f"""hi {row['name']}This is the content of the email""",'txt_sms.txt']
    yag.send(to=row["email"], subject=subject, contents=contents)
    print("send email")



# while True:
#     now = dt.now()
#     if now.hour ==17 and now.minute ==41:
#         yag.send(to=reseiver, subject=subject, contents=contents)
#         print("Email Send")
#         time.sleep(60)