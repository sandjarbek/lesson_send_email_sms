import yagmail
import os
import time
from _datetime import datetime as dt
import pandas

sender = "sanjarbek.soatov1989@gmail.com"







yag = yagmail.SMTP(user=sender, password=os.getenv("PASSWORD"))

df = pandas.read_csv("content1.csv")


print(df)

def generate_file(filename, content):
    with open(filename, 'w') as file:
        file.write(str(content))


for index, row in df.iterrows():
    name = row['name']
    filename = name +".txt"
    amount = row['amount']
    generate_file(filename, amount)
    subject = "This is the subject"
    contents = [f"""hi {name}This is the content of the emai, aomount of the content - {amount}""", filename]
    yag.send(to=row["email"], subject=subject, contents=contents)
    print("send email")
