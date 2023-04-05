# subscribe to amqp
# Listen to user status updates
# [AMQP] *.status

# Get family
# [GET] /user/family/{familyID}

# send email
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
from amqp_helper import Rabbitmq

import os
import smtplib

# Get the value of the "MY_VAR" environment variable
load_dotenv()
EMAIL = os.getenv("EMAIL")
EMAIL_PASSWORD =  os.getenv("EMAIL_PASSWORD")

def send_email(subject, message, from_addr, to_addr, password, smtp_server='smtp.gmail.com', smtp_port=587):
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_addr
    msg['To'] = to_addr

    # Create the body of the message (a plain-text and an HTML version).
    text = message
    html = f"""\
    <html>
        <head></head>
        <body>
            <p>{message}</p>
        </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    msg.attach(part1)
    msg.attach(part2)

    # Create SMTP connection.
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.ehlo()
        server.starttls()
        server.login(from_addr, password)
        server.sendmail(from_addr, to_addr, msg.as_string())

    print("Email sent successfully!")

def send_email_callback(ch, method, properties, body):
    pass

def main():
    rabbitmq = Rabbitmq()
    rabbitmq.subscribe('All User Status',send_email_callback)

if __name__ == "__main__":

    subject = "Test Email"
    message = "This is a test email sent from Python!"
    from_addr = EMAIL
    to_addr = "joeytanbiz@outlook.com"
    password = EMAIL_PASSWORD

    send_email(subject, message, from_addr, to_addr, password)
