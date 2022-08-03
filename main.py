from dotenv import load_dotenv
import os
import smtplib
import ssl
load_dotenv()


SMAIL = os.environ.get('SMAIL')
PORT = os.environ.get('PORT')
RMAIL = 'pavanponnaganti2002@gmail.com'
PASSWORD = os.environ.get('PASSWORD')
smtp_server = 'smtp.gmail.com'

msg = """\
Subject: Hi there

This message is sent from Python."""

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, PORT, context=context) as server:
    server.login(SMAIL, PASSWORD)
    server.sendmail(SMAIL, RMAIL, msg)
