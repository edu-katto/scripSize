from email.message import EmailMessage
from decouple import config
import smtplib 

# Create an email message object 
message = EmailMessage()

message['From'] = config('EMAIL_SEND_MESSAGE')
message['To'] = config('EMAIL_TO')

# Set smtp server and port
server = smtplib.SMTP(config('EMAIL_SMTP'), config('EMAIL_SMTP_PORT'))

# Identify this client to the SMTP server 
server.ehlo() 

# Secure the SMTP connection 
server.starttls()


def sendMail(emailSubject, contentEmail):

    message['Subject'] = emailSubject
    # Set email body text 
    message.set_content(contentEmail)

    # Login to email account 
    server.login(config('EMAIL_SEND'), config('EMAIL_PASS')) 

    # Send email 
    server.send_message(message) 

    # Close connection to server 
    server.quit()