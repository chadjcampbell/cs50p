from datetime import date
import sys
import re
import inflect

p = inflect.engine()


def main():
    bday = input("Date of birth: ")
    if re.match(r"\d{4}-\d{2}-\d{2}", bday):
        today = date.today()
        print(minutes(date.fromisoformat(bday), today))
    else:
        sys.exit("Invalid date")
    
def minutes(bday,today):
    diff = today - bday
    words = p.number_to_words(diff.days * 24 * 60, andword="")
    return f"{words.capitalize()} minutes"



if __name__ == "__main__":
    main()