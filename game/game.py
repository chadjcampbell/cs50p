import random
import sys

def main():
    while True:
        try:
            level = int(input('Level: '))
            if level <= 0:
                continue
            winner = random.randrange(1,level+1)
            while True:
                try:
                    guess =int(input('Guess: '))
                    if (guess < winner):
                        print('Too small!')
                    if guess > winner:
                        print('Too large!')
                    if guess == winner:
                        print('Just right!')
                        sys.exit()
                except TypeError and ValueError:
                    continue
        except TypeError and ValueError:
            continue


main()