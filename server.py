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
                display.clear('Wrong Personal email or Password'.upper())
                my_email = str(input('\nPersonal Email: '))
                my_pswd  = getpass.getpass('Your Password: ')
                msg['From'] = my_email
            else:
                break

        text = msg.as_string()

        # while True:
        #     try:
        #         server.sendmail(my_email, dest_email, text)
        #     except Exception as e:
        #         # display.clear('\nBe sure to allow less secure apps and try again \nhttps://myaccount.google.com/lesssecureapps')
        #         print(e)
        #         print('destination email {0} not valid'.format(dest_email))
        #         # display.clear('')
        #         time.sleep(10)
        #
        #     server.quit()
        #     break
        server.sendmail(my_email, dest_email, text)
        server.quit()
