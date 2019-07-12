import getpass
import content

email = content.Messenger()

class Data():
    def __init__(self):
        pass

    def get(self):
        print('\nPERSONAL DATA ...')
        my_email = str(input('Your Email: '))
        my_pswd  = getpass.getpass('Your Password:')


        send_to = str(input('\nTo Email: '))
        subject = str(input('Subject:  '))
        message = str(input('Message:  '))

        email.cont(my_email, my_pswd, send_to, subject, message)
