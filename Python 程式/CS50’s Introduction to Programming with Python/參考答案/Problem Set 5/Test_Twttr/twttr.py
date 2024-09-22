# Implement a program that prompts the user for a str of text and then outputs
# that same text but with all vowels (A, E, I, O, and U) omitted, whether
# inputted in uppercase or lowercase.

from typing import Final


VOWELS : Final[list[str]] = ["A", "E", "I", "O", "U"]


def shorten(line : str) -> str:
    for character in line:
        if character.upper() in VOWELS:
            line = line.replace(character, "")

    return line


def main() -> None:
    line : str = input("Input: ")

    line = shorten(line)

    print(f"Output: {line}")


if __name__ == "__main__":
    shorten()
