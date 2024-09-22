# If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100. Ignore any leading whitespace in the user’s greeting,
# and treat the user’s greeting case-insensitively.


def value(line : str) -> str:
    if line.startswith("hello"):
        return "$0"
    elif line.startswith("h"):
        return "$20"
    else:
        return "$100"


def main() -> None:
    line : str = input("Greeting: ").strip().lower()

    result : str = value(line)

    print(result)


# Driver Code
if __name__ == "__main__":
    main()
