import smtplib, os, server, file
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

file = file.File()
serv = server.Server()

class Messenger():
    def __init__(self):
        pass

    def mail_content(self, my_email, my_pswd, dest_email, subject, message):
        msg = MIMEMultipart()
        msg['From']    = my_email
        msg['To']      = dest_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        any_file = str(input("\nAttach a file (yes, no): "))
        if any_file.lower() == 'yes':
            msg.attach(file.annex())


        print('\n\nSending ...', end='')
        serv.deliver(msg, my_email, my_pswd, dest_email)
