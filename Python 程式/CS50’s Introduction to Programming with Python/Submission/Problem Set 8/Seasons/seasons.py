import datetime
import inflect
import sys


def checkDays(input_day) -> int:

    try:
        input_day : str = datetime.date.fromisoformat(input_day)
    except ValueError:
        sys.exit("Invalid date")

    today : str = datetime.date.today()
    minutes : int = ((today - input_day).days *60 *24)
    return minutes

def printMinutes(minutes):

    print(f"{inflect.engine().number_to_words(minutes, andword = "")} minutes".capitalize())


def main():

    printMinutes(checkDays(input("Date of Birth:")))


if __name__ == "__main__":
    main()


