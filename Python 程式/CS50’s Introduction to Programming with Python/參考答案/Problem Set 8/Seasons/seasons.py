# Implement a program that prompts the user for their date of birth in YYYY-MM-DD format and then sings prints how old
# they are in minutes, rounded to the nearest integer, using English words instead of numerals, just like the song from
# Rent, without any and between words.

# Since a user might not know the time at which they were born, assume, for
# simplicity, that the user was born at midnight (i.e., 00:00:00) on that date. And assume that the current time is also
# midnight.


import inflect
import sys
from datetime import date, timedelta
from typing import Final


def calculateAgeInMinutes(birth_date : str) -> int:
    try:
        birthday : date = date.fromisoformat(birth_date)

    except ValueError:
        sys.exit("Invalid Date")

    today : date = date.today()
    days_difference : timedelta = today - birthday
    age_in_minutes : int = days_difference.days * 24 * 60

    return age_in_minutes


def printAgeInMinutes(minutes : int) -> None:
    engine : inflect.engine = inflect.engine()

    age_in_minutes : str = engine.number_to_words(minutes, andword = "").capitalize()

    print(f"{age_in_minutes} minutes")


def main() -> None:
    birthday : str = input("Date of Birth: ")

    printAgeInMinutes(calculateAgeInMinutes(birthday))


if __name__ == "__main__":
    main()