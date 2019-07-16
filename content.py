import smtplib, os, server, file
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

file = file.File()
serv = server.Server()

class Messenger():
    def __init__(self):
        self.attached = False
        self.files_attached = 0

    def mail_content(self, my_email, my_pswd, dest_email, subject, message):
        for email in dest_email:
            msg = MIMEMultipart()
            msg['From']    = my_email
            msg['To']      = email
            msg['Subject'] = subject
            msg.attach(MIMEText(message, 'plain'))

            while self.attached == False:
                if self.files_attached == 0:
                    any_file = str(input("\nAdd file (yes, no): "))
                else:
                    any_file = str(input("\nAdd more (yes, no): "))

                if any_file.lower().startswith('y'):
                    if file.annex != False:
                        msg.attach(file.annex())
                        self.files_attached += 1

                elif any_file.lower().startswith('n'):
                    self.attached = True
                else:
                    print('Invalid input')

            print('\nSending emails with {0} attachments...'.format(self.files_attached), end='')
            serv.deliver(msg, my_email, my_pswd, dest_email)
            break
