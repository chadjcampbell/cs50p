import sys
import csv


def main():
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if not sys.argv[1].endswith('.csv'):
        sys.exit('Not a CSV file')
    try:
        with open(sys.argv[1]) as file:
            reader = csv.DictReader(file)
            students = []
            for row in reader:
                last, first = row['name'].split(',')
                students.append([first, last, row['house']])
            with open(sys.argv[2], 'w') as wFile:
                fieldnames = ['first', 'last', 'house']
                writer = csv.DictWriter(wFile, fieldnames=fieldnames)
                writer.writeheader()
                for s in students:
                    writer.writerow(
                        {'first': s[0].strip(), 'last': s[1].strip(), 'house': s[2].strip()})

    except:
        sys.exit(f'Could not read {sys.argv[1]}')


if __name__ == "__main__":
    main()
