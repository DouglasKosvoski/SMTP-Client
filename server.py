import smtplib

class Server():
    def __init__(self):
        pass

    def deliver(self, msg, my_email, my_pswd, dest_email):
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(my_email, my_pswd)
        text = msg.as_string()
        server.sendmail(my_email, dest_email, text)
        server.quit()
