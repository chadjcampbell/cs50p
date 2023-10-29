def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(str):
    nums_count = 0
    if (not str[0].isalpha() and not str[1].isalpha()):
        return False
    if (len(str) < 2 or len(str) > 6):
        return False
    for s in str:
        if s.isdigit():
            if nums_count == 0 and s == '0':
                return False
            nums_count += 1
    if has_digits_in_middle(str):
        return False
    for s in str:
        if not s.isalnum():
            return False
    return True


def has_digits_in_middle(str):
    nums = 0
    for s in str:
        if s.isdigit():
            nums += 1
        if s.isalpha() and nums > 0:
            return True
    return False


main()
