# Implement a program that:

# Expects zero or two command-line arguments:
#   Zero if the user would like to output text in a random font.

#   Two if the user would like to output text in a specific font,
#   in which case the first of the two should be -f or --font, and
#   the second of the two should be the name of the font.
#
# Prompts the user for a str of text.
# Outputs that text in the desired font.
# If the user provides two command-line arguments and the first is not -f
# or --font or the second is not the name of a font, the program should exit
# via sys.exit with an error message.

import sys
from pyfiglet import Figlet

def checkArgumentCount(length : int) -> bool:
    return length == 1 or length == 3


def checkArgument(arguments : list) -> bool:
    available_font : list[str] = Figlet().getFonts()

    if arguments[1] != "-f" and arguments[1] != "--font":
        return False

    if arguments[2] not in available_font:
        return False

    return True


def main() -> None:
    argument_length : int = len(sys.argv)

    if not checkArgumentCount(argument_length):
        sys.exit("Invalid Argument Count.")

    if argument_length == 3 and not checkArgument(sys.argv):
        sys.exit("Invalid Arguments")

    line : str = input("Input: ")

    figlet : Figlet = Figlet()

    if argument_length == 3:
        figlet.setFont(font = sys.argv[2])

    print(figlet.renderText(line))


if __name__ == "__main__":
    main()