import sys


def main():
    names = []
    while True:
        try:
            names.append(input('Name: '))
        except EOFError:
            print('Adieu, adieu, to ', end='')
            if len(names) == 1:
                print(names[0])
                sys.exit()
            if len(names) == 2:
                print(f'{names[0]} and {names[1]}')
                sys.exit()
            for i, name in enumerate(names):
                if i == len(names) - 1:
                    print(f'and {name}')
                    sys.exit()
                print(name, end=', ')
            sys.exit()


main()
