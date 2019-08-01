#! python3
# mapIt.py - Launches a map in the browser using an address from the command line
# or clipboard

import webbrowser, sys, pyperclip
if len(sys.argv) >1:
    #get address from command line. 
    address = ''.join(sys.argv[1:])

#TODO get address from clipboard
else:
    address = pyperclip.paste()

webbrowser.open('http://www.google.com/maps/place/' + address)
