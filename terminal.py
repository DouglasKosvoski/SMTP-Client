from subprocess import call
import os

class Screen:
    def __init__(self):
        pass

    def clear(self, t=''):
        _ = call('clear' if os.name =='posix' else 'cls')
        print('\033c', end=t)
