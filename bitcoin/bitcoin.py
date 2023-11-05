import requests
import sys

def main():
    if len(sys.argv) != 2:
        sys.exit('Missing command-line argument')
    if not is_float(sys.argv[1]):
        sys.exit('Command-line argument is not a number')
    multi = float(sys.argv[1])
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        price = r.json()['bpi']['USD']['rate_float']
        total = price * multi
        print(f'${total:,.4f}')
    except requests.RequestException:
        sys.exit('API call failed')

def is_float(string):
    try:
        float(string)
        return True
    except ValueError:
        return False

if __name__ == "__main__":
    main()