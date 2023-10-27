def main():
    ans = input(
        'What is the Answer to the Great Question of Life, the Universe, and Everything? ')
    if ans == '42':
        print('Yes')
    elif ans.lower() == 'forty-two':
        print('Yes')
    elif ans.lower() == 'forty two':
        print('Yes')
    else:
        print('No')


main()
