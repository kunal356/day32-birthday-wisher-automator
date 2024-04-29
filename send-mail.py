import smtplib
import datetime as dt
import random

#
# my_email = "gaikwadkunal1@yahoo.com"
my_email = "kunal.gaikwad970@gmail.com"
password = "waui jtwe ceqz srre"  ## gmail app password
weekdays = {
    0: "Monday",
    1: "Tuesday",
    2: "Wednesday",
    3: "Thursday",
    4: "Friday",
    5: "Saturday",
    6: "Sunday",
}


def send_email(quote, day):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="gaikwadkunal1@yahoo.com",
                            msg=f"Subject:{day} Motivation\n\n {random_quote}"
                            )


today_date = dt.datetime.now()
today_day = weekdays.get(today_date.weekday())
if today_day == "Monday":
    with open('quotes.txt') as data:
        quote_list = [line.strip() for line in data.readlines()]
        random_quote = random.choice(quote_list)
        send_email(random_quote, today_day)
