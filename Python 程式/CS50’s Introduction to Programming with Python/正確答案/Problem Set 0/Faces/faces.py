# Define a function called "convert" that converts input to emoticons

# Converts input to emoticons
def convert(input : str) -> str:

    return input.replace(":)", "\U0001F642").replace(":(", "\U0001F641")


def main() -> None:
    line : str = input()

    print(convert(line))


if __name__ == "__main__":
    main()
