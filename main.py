import terminal
import data

if __name__ == '__main__':
    t = terminal.Screen()
    info = data.Data()

    t.clear('''AUTOMATED EMAIL by DOUGLAS KOSVOSKI
GIT REPO https://github.com/DouglasKosvoski/Terminal_Email
REMEMBER TO ALLOW THE APP https://myaccount.google.com/lesssecureapps
''')

    info.get()

t.clear()
