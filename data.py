import getpass
import content

email = content.Messenger()

class Data():
    def __init__(self):
        pass

    def get(self):
        my_email = str(input('\nPersonal Email: '))
        my_pswd  = getpass.getpass('Your Password : ')

        send_to = list(map(str, input('\nEmail Destination: ').split(', ')))
        subject = str(input('Subject: '))
        message = str(input('Message: '))

        email.mail_content(my_email, my_pswd, send_to, subject, message)
