def main():
    str = input('Input: ')
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    new = ''
    for s in str:
        if s not in vowels:
            new += s

    print(new)


main()
