# birthday_wisher
This is a birthday wisher made by Python. To use, 'smtplib' library installation required.

## Function
- Send mail automatically to the birthday-person
- For automation, you need to run the code on Cloud. e.g., Python Anywhere: https://www.pythonanywhere.com/

## Setup
- Edit the birthday information birthdays.csv.
- Change the information below
  - SENDER_NAME = 'John Doe'
  - MY_EMAIL = 'example@gmail.com'
  - TO_EMAIL = 'example@gmail.com'
  - PASSWORD = 'example'
- Also you might need to change:
  - Argments of [smtplib.SMTP('smtp.gmail.com', 587)] depending on the mail server you use
  - Setting of the security level of your mail server

Comfirmed to work on:
- MacOS (11.52)
- PyCharm 2021.02 (Community Edition)
