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
from invokes import invoke_http
from servicehelper import isServiceReady, serviceIsReady
from time import sleep

import os
import smtplib
import json

# Get the value of the "MY_VAR" environment variable

EMAIL = os.environ.get("EMAIL")
EMAIL_PASSWORD =  os.environ.get("EMAIL_PASSWORD")

def send_email(subject, message, to_addr, from_addr=EMAIL, password=EMAIL_PASSWORD, smtp_server='smtp.gmail.com', smtp_port=587):
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

def getUsersByFamily(familyID):

    try:
        result = invoke_http(f"http://localhost:5001/user/family/{str(familyID)}","GET")
        code = result['code']

        if code in range(200,300):
            return result
        else:
            print(result)
            return []

    except Exception as e:
        print(e)

    return []

def send_email_callback(ch, method, properties, body):
    routing_key = method.routing_key
    familyID = routing_key.split('.')[1]

    users = getUsersByFamily(familyID)

    data = json.dumps(body)

    alert_data = data['alert']
    alert_name = alert_data['name']
    alert_country = alert_data['country']

    affected_userID = data['userID']
    affected_userData = [user for user in users if user['data']['userID']==affected_userID][0]
    affected_userData_name = affected_userData['name']

    for user in users:
        user_data = user['data']
        userID = user_data['userID']

        if userID != affected_userID:
            email = user_data['email']
            subject = f"{affected_userData_name} has been affected by {alert_name}"
            message = f"{affected_userData_name} has been affected by {alert_name} at {alert_country}"

            send_email(
                subject,
                message,
                email
            )

        

    


    pass

def main():
    rabbitmq = Rabbitmq()
    rabbitmq.subscribe('family_all',send_email_callback)

if __name__ == "__main__":
    while not isServiceReady("user"):
        sleep(1)
    main()
    serviceIsReady("sendemail")
