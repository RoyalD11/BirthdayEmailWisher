# 1. Update the birthdays.csv with your friends & family's details.

# Imports
import pandas
import random
import smtplib
import datetime as dt

# GLOBALS
EMAIL = ''
PASS = ""

# Get Today's Date
today = dt.datetime.now()

# Get the birthdays data and make a dictionary out of it
data = pandas.read_csv("birthdays.csv")
birthdays = data.to_dict(orient='records')


# 2. Check if today matches a birthday in the birthdays.csv

for items in birthdays:
    if items['month'] == today.month and items["day"] == today.day:

        letterChoice = random.randint(1,3)

        # Opens a text file based on a random number
        with open(f"letter_templates/letter_{letterChoice}.txt") as letterFile:

            # Reads the text file, saves the data as a list
            letterList = letterFile.readlines()

            # Create a string from the list
            letter = ''.join(word for word in letterList)

            # Replaces the [NAME] field with the persons name
            letter = letter.replace("[NAME]", items['name'])
            print(letter)

# 4. Send the letter generated in step 3 to that person's email address.
            with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
                connection.starttls()
                connection.login(EMAIL, PASS)
                connection.sendmail(
                    from_addr=EMAIL,
                    to_addrs=items["email"],
                    msg=f"Subject: Happy Birthday!\n\n{letter}"
                )


