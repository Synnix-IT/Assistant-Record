# Implement a program that:

# Expects the user to provide two command-line arguments:
#   the name of an existing CSV file to read as input, whose columns are assumed to be, in order, name and house, and
#   the name of a new CSV to write as output, whose columns should be, in order, first, last, and house.

# Converts that input to that output, splitting each name into a first name and last name. Assume that each student
# will have both a first name and last name.

# If the user does not provide exactly two command-line arguments, or if the first cannot be read,
# the program should exit via sys.exit with an error message.


import csv
import sys
from typing import Final, List


SUPPOSED_ARGUMENTS_COUNT : Final[int] = 3


def checkArguments(argument : List[str]) -> None:
    length : int = len(argument)

    if length < SUPPOSED_ARGUMENTS_COUNT:
        sys.exit("Too few command-line arguments")
    elif length > SUPPOSED_ARGUMENTS_COUNT:
        sys.exit("Too many command-line arguments")

    if not argument[1].endswith(".csv"):
        sys.exit("Not a CSV file")


def writeCSVFile(csv_reader : csv.DictReader[str], csv_writer : csv.DictWriter[str]) -> None:
    for row in csv_reader:
        try:
            last_name, first_name = map(str.strip, row["name"].split(","))
            house : str = row["house"]

            csv_writer.writerow({"first" : first_name, "last" : last_name, "house" : house})

        except ValueError:
                sys.exit("Incorrect formatted name in the input file")



def processCSVFile(input_file : str, output_file : str) -> None:
    try:
        with open(input_file, "r") as csv_input, open(output_file, "w+", newline = "") as csv_output:
            csv_reader : csv.DictReader[str] = csv.DictReader(csv_input)

            field_names = ["first", "last", "house"]
            csv_writer : csv.DictWriter[str] = csv.DictWriter(csv_output, fieldnames = field_names)
            csv_writer.writeheader()

            writeCSVFile(csv_reader, csv_writer)

    except FileNotFoundError:
        sys.exit(f"Could not read file: {input_file}")


def main():
    checkArguments(sys.argv)

    input_file : str = sys.argv[1]
    output_file  : str = sys.argv[2]

    processCSVFile(input_file, output_file)


if __name__ == "__main__":
    main()