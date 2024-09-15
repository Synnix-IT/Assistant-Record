# Implement a program that prompts the user for a str in English and then outputs the “emojized” version of that str,
# converting any codes (or aliases) therein to their corresponding emoji.

from emoji import emojize

def main() -> None:
    line : str = input("Input: ")

    print(f"Output: {emojize(line, language = "alias")}")


if __name__ == "__main__":
    main()