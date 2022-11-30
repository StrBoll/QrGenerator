import pyqrcode
import png
from pyqrcode import QRCode

user_input = input('Paste the link you would like to create a QR code for: ')

link = pyqrcode.create(user_input)

# since there are characters that you cannot use while naming a file, we use a while loop try, except block

check_file_name = True

while check_file_name:
    try:
        file_name = input('\nWhat would you like to name the file?  \n')
        no_go_alphabet = ["*", "|", "<", ">", ":", "/", "?"]

        for character in file_name:
            if character in no_go_alphabet:
                raise ValueError
        check_file_name = False

    except ValueError:
        print('\nThere are invalid character(s) in the file name chosen, please rename the file.')
        check_file_name = True

    # if the user tries to save their file with characters that aren't allowed to be used, it will repeatedly ask
    # for a file name until a suitable name is entered

file_format = True

while file_format:
    try:
        format_name = int(input('''\nFile Format Menu:
-----------------
1. .svg file
2. .png file

Enter 1 or 2 to choose file format: '''))
        if format_name > 2 or format_name < 1:
            raise ValueError
        file_format = False
    except ValueError:
        print('Choose either 1 or 2 ')

    finally:
        if format_name == 1:
            file_name += '.svg'
            link.svg(file_name, scale=8)
            print(link.terminal(quiet_zone=1))
        elif format_name == 2:
            file_name += '.png'
            link.png(file_name, scale=6)
            print(link.terminal(quiet_zone=1))
            png_rendering = pyqrcode.create(user_input, error='L', version=3, mode='binary')
            png_rendering.show()

# code for saving png file to pc and displaying qr code on screen
# this can be customized in so many ways, and can even be configured to where a user could input their own customization
# through the user interface



