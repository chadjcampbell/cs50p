import sys


def main():
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if not sys.argv[1].endswith('.py'):
        sys.exit('Not a Python file')
    try:
        count = 0
        with open(sys.argv[1]) as file:
            for line in file:
                if line.strip().startswith('#') or line.strip() == '':
                    continue
                count += 1
    except:
        sys.exit('File does not exist')

    print(count)


if __name__ == "__main__":
    main()
