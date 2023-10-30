def main():
    items = dict(sorted(get_items().items()))
    for i in items:
        print(f'{items[i]} {i.upper()}')


def get_items():
    items = {}
    while True:
        try:
            item = input().lower()
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
        except EOFError:
            return items


main()
