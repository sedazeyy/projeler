import datetime as dt
import pandas
import random
import smtplib
from dotenv import load_dotenv
import os

# .env dosyasındaki değişkenleri yükle
load_dotenv()
MY_EMAIL = os.getenv("MY_EMAIL")
MY_PASSWORD = os.getenv("MY_PASSWORD")

# Bugünün tarihini al
now = dt.datetime.now()
month_day = (now.month, now.day)

# Doğum günü verilerini oku
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(row["month"], row["day"]): row for (index, row) in data.iterrows()}

# Bugün doğum günü olan biri varsa
birthday_person = birthdays_dict.get(month_day)
if birthday_person is not None:
    random_num = random.randint(1, 3)
    random_letter = f"letter_{random_num}.txt"

    with open(f"./letter_templates/{random_letter}", "r") as file:
        letter_data = file.read()

    letter_data = letter_data.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.outlook.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject: Happy Birthday!\n\n{letter_data}"
        )
    print(f"{birthday_person['name']} için doğum günü maili gönderildi!")
else:
    print("Bugün doğum günü olan kimse yok.")