import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 2:
        sys.exit('Too few command-line arguments')
    if not sys.argv[1].endswith('.csv'):
        sys.exit('Not a CSV file')
    try:
        table = []
        with open(sys.argv[1]) as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    headers = row
                    continue
                table.append(row)
        print(tabulate(table, headers, tablefmt="grid"))
    except:
        sys.exit('File does not exist')


if __name__ == "__main__":
    main()
