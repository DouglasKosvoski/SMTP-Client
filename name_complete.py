import readline
import glob

class Completer(object):
    def __init__(self):
        readline.set_completer_delims('\t')
        readline.parse_and_bind("tab: complete")

    def path_completer(self,text,state):
        line = readline.get_line_buffer().split()
        # files = '/' + ((list(asd.split('/')))[-1])
        # print('\n', files, '\n', end='')
        return [x for x in glob.glob(text+'*')][state]
