import random


def main():
    score = 0
    level = get_level()
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        correct = x + y
        attempts = 0
        while True:
            try:
                ans = input(f'{x} + {y} = ')
                if int(ans) == correct:
                    score += 1
                    break
                else:
                    attempts += 1
                    print('EEE')
                    if attempts == 3:
                        print(f'{x} + {y} = {correct}')
                        break
            except ValueError:
                attempts += 1
                print('EEE')
                if attempts == 3:
                    print(f'{x} + {y} = {correct}')
                    break
                else: 
                    continue
    print(f'Score: {score}')



def get_level():
    good = ['1','2','3']
    while True:
        level = input('Level: ')
        if level in good:
            return int(level)


def generate_integer(level):
    if level == 1:
        min = 0
        max = 9
    elif level == 2:
        min = 10
        max = 99
    else:
        min = 100
        max = 999
    return random.randint(min, max)


if __name__ == "__main__":
    main()