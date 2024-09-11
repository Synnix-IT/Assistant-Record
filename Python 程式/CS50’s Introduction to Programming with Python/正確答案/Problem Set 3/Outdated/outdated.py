# Implement a program that prompts the user for a date, in month-day-year order,
# formatted like 9/8/1636 or September 8, 1636.

# Then output that same date in YYYY-MM-DD format. If the user’s input is not a
# valid date in either format, prompt the user again. Assume that every month
# has no more than 31 days; no need to validate whether a month has 28, 29, 30,
# or 31 days.

from typing import Final, Union

MONTH : Final[list[str]] = [

    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

SLASH : Final[int] = 1
COMMA : Final[int] = 2


def checkMonth(month : str, form : int) -> bool:
    try:
        if (form == COMMA and month in MONTH) or (form == SLASH and 1 <= int(month) <= 12):
            return True
    except ValueError:
        return False

    return False


def checkDay(day : str) -> bool:
    try:
        return 1 <= int(day) <= 31
    except ValueError:
        return False


def main() -> None:
    while True:
        date : str = input("Date: ").strip()

        month : str = None
        day : str = None
        year : str = None
        form : int = None

        if "/" in date:
            month, day, year = date.split("/")
            form = SLASH
        elif "," in date:
            month, day, year = date.replace(",", "").split()
            form = COMMA

        if checkMonth(month, form) and checkDay(day):
            break

    if month in MONTH:
        month = MONTH.index(month) + 1

    month = str(month).zfill(2)
    day = str(day).zfill(2)

    print(f"{year}-{month}-{day}")


if __name__ == "__main__":
    main()
