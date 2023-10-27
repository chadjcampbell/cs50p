def main():
    param = input('File name: ').lower().strip()
    if param.endswith('.gif'):
        print('image/gif', end='')
    elif param.endswith('.jpeg'):
        print('image/jpeg', end='')
    elif param.endswith('.jpg'):
        print('image/jpeg', end='')
    elif param.endswith('.png'):
        print('image/png', end='')
    elif param.endswith('.pdf'):
        print('application/pdf', end='')
    elif param.endswith('.txt'):
        print('text/plain', end='')
    elif param.endswith('.zip'):
        print('application/zip', end='')
    else:
        print('application/octet-stream')


main()
