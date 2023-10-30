def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]
    while True:
        try:
            str = input('Date: ').strip()
            if str[-5] == '/':
                m, d, y = str.split('/')
                if wrong_format(d, m):
                    raise
            else:
                m, d, y = str.split()
                d = d[:-1]
                if m not in months:
                    raise
                m = months.index(m) + 1
                if wrong_format(d, m):
                    raise
        except:
            pass
        else:
            m = make_double_digit(int(m))
            d = make_double_digit(int(d))
            print(f'{y}-{m}-{d}')
            break


def wrong_format(d, m):
    if 1 > int(d) or int(d) > 31:
        return True
    if 1 > int(m) or int(m) > 12:
        return True
    return False


def make_double_digit(n):
    if n < 10:
        return "0" + str(n)
    else:
        return str(n)


main()
