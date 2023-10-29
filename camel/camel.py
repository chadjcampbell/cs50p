def main():
    str = input('camelCase: ')
    snake = camel_to_snake(str)
    print(f'snake_case: {snake}')


def camel_to_snake(str):
    snake = ''
    for s in str:
        if s.isupper():
            snake += '_'
        snake += s
    return snake.lower()


main()
