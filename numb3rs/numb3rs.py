import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    matches = re.search(r"(.+)\.(.+)\.(.+)\.(.+)", ip)
    if matches:
        try:
            for group in matches.groups():
                if 0 > int(group) or int(group) > 255:
                    return False
            return True
        except ValueError:
            return False
    else:
        return False


if __name__ == "__main__":
    main()
