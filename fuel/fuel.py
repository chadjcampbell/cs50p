def main():
    while True:
        try:
            f = input('Fraction: ')
            num = convert(f)
            break
        except:
            pass
    print(gauge(num))


def convert(fraction):
    arr = fraction.split('/')
    x, y = arr[0], arr[1]
    if not x.isnumeric() or not y.isnumeric():
        raise ValueError
    if int(x) / int(y) > 1:
        raise ValueError
    if (int(x) > 0 and int(y) == 0):
        raise ZeroDivisionError
    return round(int(x) / int(y) * 100)


def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return f'{percentage}%'


if __name__ == "__main__":
    main()
