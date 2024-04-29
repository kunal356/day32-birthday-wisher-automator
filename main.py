import datetime as dt
import pandas as pd
import smtplib
import random

MY_EMAIL = "kunal.gaikwad970@gmail.com"
MY_PASSWORD = "1234" # Replace app password
birthdays_record = pd.read_csv('birthdays.csv')
birthdays_record = birthdays_record.to_dict(orient="records")
now = dt.datetime.now()
month = now.month
day = now.day

random_num = random.randint(1, 3)
print(f"letter_templates/letter_{random_num}.txt")
with open(f"letter_templates/letter_{random_num}.txt") as letter:
    content = letter.readlines()

    for i in birthdays_record:
        if i['month'] == month and i['day'] == day:
            content = ''.join(content).replace("[NAME]", i['name'])
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=i['email'],
                    msg=f"Subject: Happy Birthday!!!! \n\n {content}"
                )
