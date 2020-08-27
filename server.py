import smtplib, getpass, terminal

class Server():
    def __init__(self):
        pass

    def deliver(self, msg, my_email, my_pswd, dest_email):
        display = terminal.Screen()
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()

        while True:
            try:
                server.login(my_email, my_pswd)
            except Exception as e: # wrong email, pswd
                display.clear()
                print('REMEMBER TO ALLOW THE APP AT https://myaccount.google.com/lesssecureapps\nAND RESTART THE APPLICATION',
                '\n\nWrong Personal email or Password'.upper())
                my_email = str(input('\nPersonal Email: '))
                my_pswd  = getpass.getpass('Your Password: ')
                msg['From'] = my_email
            else:
                break

        text = msg.as_string()

        server.sendmail(my_email, dest_email, text)
        server.quit()
