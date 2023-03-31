import os
from email.message import EmailMessage
import ssl
import smtplib

#variables
email_sender = 'bracichowiczaleksandra@gmail.com'
email_password = os.environ.get("EMAIL_PASSWORD")
email_receiver = 'bracichowiczola@gmail.com'
subject = 'TEST - MAIL Z PYTHONA'
body = """
test



test



:D

"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['Subject'] = subject
em.set_content(body)

#add ssl
context = ssl.create_default_context()

#sending an email
with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())