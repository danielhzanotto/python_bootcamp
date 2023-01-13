# get list of birtdays
# see if there's some birthday today
# get a random letter
# change Letter info with person's info
# send letter to person's email

import pandas as pd
import datetime as dt
import random
import smtplib

MY_EMAIL = "mmegaterio@gmail.com"
MY_PASSWORD = "zkyhcquwdplsxzkj"

now = dt.datetime.now()
day = now.day
month = now.month

friends_list = pd.read_csv("birthdays.csv")

friends_dict = friends_list.to_dict("records")

for friend in friends_dict:
    if friend["month"] == month and friend["day"] == day:
        friend_of_the_day = friend

        random_letter = random.randint(1, 3)

        with open(f"letter_templates/letter_{random_letter}.txt") as dt:
            letter = dt.read()
            new_letter = letter.replace("[NAME]", friend_of_the_day["name"])
            print(new_letter)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=friend_of_the_day["email"],
                                msg=f"Subject: Happy Birthday!!\n\n{new_letter}")
