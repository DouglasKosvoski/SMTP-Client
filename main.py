import terminal
import data

if __name__ == '__main__':
    display = terminal.Screen()
    info = data.Data()

    display.clear('''AUTOMATED EMAIL by DOUGLAS KOSVOSKI
GIT REPO https://github.com/DouglasKosvoski/Terminal_Email
REMEMBER TO ALLOW THE APP AT https://myaccount.google.com/lesssecureapps
''')

    info.get()

display.clear()
