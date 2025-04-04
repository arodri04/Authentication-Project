import os
from email.message import EmailMessage
import ssl
import smtplib
from dotenv import load_dotenv


def sendEmail(email, number):
    load_dotenv()

    password = os.environ['PASSWORD']
    body = f"Please enter this 6 digit number: {number}"


    em = EmailMessage()

    em['From'] = 'ict350emailtest@gmail.com'
    em['To'] = email
    em['Subject'] = "Authentication Required"
    em.set_content(body)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
        smtp.login('ict350emailtest@gmail.com', password)
        smtp.sendmail('ict350emailtest@gmail.com', email, em.as_string())