import sys
import os
from PIL import Image, ImageOps


def main():
    if len(sys.argv) > 3:
        sys.exit('Too many command-line arguments')
    if len(sys.argv) < 3:
        sys.exit('Too few command-line arguments')
    if not checkExtValid(sys.argv[1]) or not checkExtValid(sys.argv[2]):
        sys.exit('Invalid input or output')
    if os.path.splitext(sys.argv[1])[1] != os.path.splitext(sys.argv[2])[1]:
        sys.exit('Input and output have different extensions')
    try:
        with Image.open(sys.argv[1]) as image:
            size = (600, 600)
            image = ImageOps.fit(image, size)
            shirt = Image.open("shirt.png")
            image.paste(shirt, shirt)
            image.save(sys.argv[2])
    except:
        sys.exit('Input does not exist')


def checkExtValid(str):
    exts = ['.jpg', '.jpeg', '.png']
    extension = os.path.splitext(str)[1]
    if extension in exts:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
