def main():
    total = 0
    valid = [5, 10, 25]
    while total < 50:
        print(f'Amount Due: {50-total}')
        coin = int(input('Insert Coin: '))
        if (coin in valid):
            total += coin
    print(f'Change Owed: {total-50}')


main()
