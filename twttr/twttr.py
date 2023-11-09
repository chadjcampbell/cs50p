def main():
    str = input('Input: ')
    short = shorten(str)
    print(short)


def shorten(word):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new = ''
    for s in word:
        if s not in vowels:
            new += s

    return new


if __name__ == "__main__":
    main()
