def main():
    f = round(get_fraction('Fraction: ') * 100)
    if f < 1:
        print('E')
    elif f > 99:
        print('F')
    else:
        print(f'{f}%')


def get_fraction(prompt):
    while True:
        try:
            arr = input(prompt).split('/')
            x, y = int(arr[0]), int(arr[1])
            if (int(x) > 0 and int(y) == 0):
                raise
            if x / y > 1:
                raise
            return x / y
        except:
            pass


main()
