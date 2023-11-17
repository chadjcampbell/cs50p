import re


def main():
    print(count(input("Text: ")))


def count(s):
    return len(re.findall(r'\bum\b', s.lower(), re.MULTILINE))


if __name__ == "__main__":
    main()
