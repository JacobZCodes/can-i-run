from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
import re

def mail(recipient_address, subject, body):
    try:
        # sender_address = 'jacobzamore901@gmail.com'
        # sender_password = 'veqo pdqz qyrd usvh' # Email To Text password granting full access to the SMTP server for my personal email address, but we will create a power2peoplegmail so it looks legit\

        sender_address = 'power.to.people.2024@gmail.com'
        sender_password = 'aokh jrou wjbb tsdb' # Email To Text Official password granting full access to the SMTP server for official email address
        

        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = recipient_address
        message['Subject'] = subject
        message.attach(MIMEText(body, 'plain'))

        text = message.as_string()

        SMTPserver = smtplib.SMTP('smtp.gmail.com', 587)
        SMTPserver.starttls()
        SMTPserver.login(sender_address, sender_password)
        SMTPserver.sendmail(sender_address, recipient_address, text)

        SMTPserver.quit()
        print('Email sent successfully!')
    except Exception as e:
        print(f'Error: {e}')

def send_text():
    recipient_address = '9494694524@vtext.com' # recipient_address changes for different cell carriers!!
    subject = 'Test Subject'
    body = 'lmk when you get this!'
    # Replace the recipient_address, subject, and body with your desired values
    mail(recipient_address, subject, body)
    print("sent text!")
