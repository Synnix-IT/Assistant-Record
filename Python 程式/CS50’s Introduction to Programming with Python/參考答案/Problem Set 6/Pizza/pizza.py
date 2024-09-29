# Implement a program that expects exactly one command-line argument, the name (or path) of a CSV file
# in Pinocchio’s format, and outputs a table formatted as ASCII art using tabulate..

# Format the table using the library’s grid format. If the user does not specify exactly one command-line
# argument, or if the specified file’s name does not end in .csv, or if the specified file does not exist,
# the program should instead exit via sys.exit.


import csv
import sys
from tabulate import tabulate
from typing import Final, List


SUPPOSED_ARGUMENTS_COUNT : Final[int] = 2


def checkArguments(argument : List[str]) -> None:
    length : int = len(argument)

    if length < SUPPOSED_ARGUMENTS_COUNT:
        sys.exit("Too few command-line arguments")
    elif length > SUPPOSED_ARGUMENTS_COUNT:
        sys.exit("Too many command-line arguments")

    if not argument[1].endswith(".csv"):
        sys.exit("Not a CSV file")


def readCSV(file_name : str) -> None:
    with open(file_name, "r") as csv_file:
        csv_reader = csv.reader(csv_file)
        headers = next(csv_reader)

        if headers is None:
            sys.exit("CSV file is empty")

        print(tabulate(csv_reader, headers = headers, tablefmt = "grid"))


def main():
    checkArguments(sys.argv)

    file_name : str = sys.argv[1]

    try:
        readCSV(file_name)

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()