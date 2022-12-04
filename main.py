import pyqrcode
import png
from pyqrcode import QRCode
import requests

#Check if the url is valid through a very simplified method

# if status of url returns 404, this means it does not work
# however, there may be other errors with the link, so we make sure the link returns 200


url = False

# if you forget to paste the http part of the link, like many do when typing links like www.xyz.com, it will
# automatically add it in for you

header_check = 'https://'
header_check2 = 'http://'

while not url:
    user_input = input('Paste the link you would like to create a QR code for: ')

    if header_check in user_input or header_check2 in user_input:
        continue
    else:
        user_input = header_check + user_input

    try:
        request = requests.get(user_input)
        status = request.status_code

        if status != 200:
            raise Exception

        # raising a general exception simply because here it is
        # not necessary to call a specific error type for the try block

        url = user_input

    except Exception:
        print('Url is broken, please check the link and re-enter\n')
        url = False


link = pyqrcode.create(url)

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


# code for saving png file to pc and displaying qr code on screen
# this can be customized in so many ways, and can even be configured to where a user could input their own customization
# through the user interface



