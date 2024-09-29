# Implement a program that expects exactly one command-line argument, the name (or path) of a Python file,
# and outputs the number of lines of code in that file, excluding comments and blank lines.

# If the user does not specify exactly one command-line argument, or if the specified file’s name does not
# end in .py, or if the specified file does not exist, the program should instead exit via sys.exit.


import sys
from typing import Final


SUPPOSED_ARGUMENTS_COUNT : Final[int] = 2


def checkArguments(argument : list[str]) -> None:
    length : int = len(argument)

    if length < SUPPOSED_ARGUMENTS_COUNT:
        sys.exit("Too few command-line arguments")
    elif length > SUPPOSED_ARGUMENTS_COUNT:
        sys.exit("Too many command-line arguments")

    if not argument[1].endswith(".py"):
        sys.exit("Not a python file")


def checkValidLine(line : str) -> bool:
    line = line.strip()

    if line.strip().startswith("#") or not line:
        return False

    return True


def countLine(file_name : str) -> int:
    line_count : int = 0

    with open(file_name, "r") as file:
        for line in file:
            if checkValidLine(line):
                line_count += 1

    return line_count


def main():
    checkArguments(sys.argv)

    file_name : str = sys.argv[1]

    try:
        line_count : int = countLine(file_name)
        print(line_count)
    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
