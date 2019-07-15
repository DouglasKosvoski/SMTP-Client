import terminal
import data

if __name__ == '__main__':
    display = terminal.Screen()
    info = data.Data()

    display.clear('''
*** REMEMBER TO ALLOW THE APP AT https://myaccount.google.com/lesssecureapps
*** GIT REPO https://github.com/DouglasKosvoski/Terminal_Email
''')

    info.get()

display.clear()
