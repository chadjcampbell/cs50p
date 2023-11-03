from pyfiglet import Figlet
import sys
from random import choice


def main():
    figlet = Figlet()
    if len(sys.argv) == 1:
        str = input('Input: ')
        font = choice(figlet.getFonts())
        figlet.setFont(font=font)
        print(figlet.renderText(str))
    elif len(sys.argv) == 3:
        if sys.argv[1] != '-f' and sys.argv[1] != '--font':
            sys.exit('Invalid usage')
        else:
            if sys.argv[2] not in figlet.getFonts():
                sys.exit('Invalid usage')
            str = input('Input: ')
            try:
                figlet.setFont(font=sys.argv[2])
                print(figlet.renderText(str))
            except:
                sys.exit('Invalid usage')
    else:
        sys.exit('Invalid usage')


main()
