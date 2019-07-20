import os, readline, path_complete
from email import encoders
from email.mime.base import MIMEBase

name = path_complete.Completer()
readline.set_completer(name.path_completer)

class File():
    def __init__(self):
        pass

    def annex(self):
        file_path = str(input("File PATH: "))

        while os.path.isfile(file_path) == False:
            if os.path.isdir(file_path) == True:
                print('Oops... You can not add a folder')
            else:
                print('Oops... File not found')
            file_path = str(input("File PATH: "))

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((open(file_path, 'rb')).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename= %s' % (os.path.basename(file_path)))
        # filename   = os.path.basename(file_path)
        # attachment = open(file_path, 'rb')
        # part = MIMEBase('application', 'octet-stream')
        # part.set_payload((attachment).read())
        # encoders.encode_base64(part)
        # part.add_header('Content-Disposition', 'attachment; filename= %s' % (filename))

        return part
