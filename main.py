import datetime as dt
import random
import pandas
import smtplib

# Change the information below
SENDER_NAME = 'John Doe'
MY_EMAIL = 'example@gmail.com'
TO_EMAIL = 'example@gmail.com'
PASSWORD = 'example'

now = dt.datetime.now()
current_month = now.month
current_day = now.day

data = pandas.read_csv('birthdays.csv')
birthday_dict = data.to_dict(orient='records')
print(birthday_dict)
for birthday_info in birthday_dict:
    name = birthday_info['name']
    email = birthday_info['email']
    # year = birthday_info['year']
    month = birthday_info['month']
    day = birthday_info['day']
    if month == current_month and day == current_day:
        with open(f'letter_templates/letter_{random.randint(1, 3)}.txt') as file:
            letter_template = file.read()
            letter = letter_template.replace('[TO_NAME]', name)
            letter = letter_template.replace('[TO_NAME]', SENDER_NAME)

        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=TO_EMAIL,
                msg='subject: Happy Birthday!\n\n'
                    f'{letter}'
            )

