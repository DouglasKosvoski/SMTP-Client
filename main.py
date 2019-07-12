import smtplib, getpass, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def clear_Screen(t=''):
    from subprocess import call
    _ = call('clear' if os.name =='posix' else 'cls')
    print('\033c', end=t)


def content(my_email, my_pswd, dest_email, subject, message):
    any_file = str(input("Wanna attach a file? (yes, no): "))
    if any_file.lower() == 'yes':
        file_path  = str(input("File PATH: "))
        filename   = os.path.basename(file_path)
        attachment = open(file_path, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename= %s' % (filename))


    print('\n\nSending ...')
    msg = MIMEMultipart()
    msg['From']    = my_email
    msg['To']      = dest_email
    msg['Subject'] = subject
    msg.attach(MIMEText(message, 'plain'))

    if any_file.lower() == 'yes':
         msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(my_email, my_pswd)
    text = msg.as_string()
    server.sendmail(my_email, dest_email, text)
    server.quit()

def get_data():
    print('\nPERSONAL DATA ...')
    my_email = str(input('Your Email: '))
    my_pswd  = getpass.getpass('Your Password:')
    print('\n\nDESTINATION DATA ...')
    send_to = str(input('To Email: '))
    subject = str(input('Subject: '))
    message = str(input('Your Message: '))

    content(my_email, my_pswd, send_to, subject, message)

clear_Screen('AUTOMATED EMAIL by ATTORY\n')
get_data()
clear_Screen()
