import smtplib
import datetime as dt
import random
import pandas as pd
import os

# Opening csv file and choosing dates:
df = pd.read_csv("birthdays.csv")
df = pd.DataFrame(df)

# Dict of months and date:
dates = {key: value for key, value in zip(df["month"], df["day"])}
today = dt.datetime.now()

# selecting random module
files = os.listdir(r"folder_path")
files_list = [file for file in files if file.endswith(".txt")]
random_file = random.choice(files_list)


# checking date and sending mail:
my_email = "your_mail"
password = "app_password"  '''--> to be obtained from manage google account<security<app passwords<set up app password'''

for index, row in df.iterrows():
    if today.month == row["month"] and today.day == row["day"]:
        # customizing:
        with open(f"root_folder_path{random_file}") as mail_format:
            content = mail_format.read()
            new_content = content.replace("[NAME]", row["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection: '''smtp for gmail addresses'''
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs="receiver's mail", msg=new_content)

