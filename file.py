import os
from email import encoders
from email.mime.base import MIMEBase

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
