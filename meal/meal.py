def main():
    str = input('What time is it? ')
    time = convert(str)
    if 7 < time < 8:
        print('breakfast time')
    elif 12 < time < 13:
        print('lunch time')
    elif 18 < time < 19:
        print('dinner time')
    else:
        return


def convert(time):
    x, y = time.split(':')
    y = int(y) / 60
    return int(x) + y


if __name__ == "__main__":
    main()
