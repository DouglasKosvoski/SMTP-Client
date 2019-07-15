import os, readline, name_complete
from email import encoders
from email.mime.base import MIMEBase

name = name_complete.Completer()
readline.set_completer(name.path_completer)

class File():
    def __init__(self):
        pass

    def annex(self):
        file_path  = str(input("File PATH: "))
        filename   = os.path.basename(file_path)
        attachment = open(file_path, 'rb')

        part = MIMEBase('application', 'octet-stream')
        part.set_payload((attachment).read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename= %s' % (filename))

        return part
