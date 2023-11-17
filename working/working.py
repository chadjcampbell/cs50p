import re


def main():
    print(convert(input("Hours: ")))


def convert(s):
    if matches := re.match(r"([\d|:]+) (\w+) to ([\d|:]+) (\w+)", s):
        start = makeTime(matches.group(1), matches.group(2))
        end = makeTime(matches.group(3), matches.group(4))
        return f"{start} to {end}"
    else:
        raise ValueError


def makeTime(time, label):
    if ':' in time:
        hr, min = time.split(':')
    else:
        hr = time
        min = "00"
    if int(hr) > 12 or int(hr) < 1 or int(min) > 59 or int(min) < 0:
        raise ValueError
    if hr == '12':
        hr = '0'
    if len(hr) == 1:
        hr = "0" + hr
    if label == "PM":
        hr = str(int(hr)+12)
    return f"{hr}:{min}"


if __name__ == "__main__":
    main()
