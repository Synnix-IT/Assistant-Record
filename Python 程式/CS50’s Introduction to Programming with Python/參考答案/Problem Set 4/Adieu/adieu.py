# Implement a program that prompts the user for names, one per line, until the
# user inputs control-d. Assume that the user will input at least one name.

# Then bid adieu to those names, separating two names with one and, three names
# with two commas and one and, and names with commas and one and


def printNames(names : list[str]) -> None:
    length : int = len(names)

    print("Adieu, adieu, to ", end = "")

    match length:
        case 1:
            print(names[0])

        case 2:
            print(f"{names[0]} and {names[1]}")

        case _:
            print(f"{', '.join(names[:-1])}, and {names[-1]}")


def main() -> None:
    names : list[str] = list()

    while True:
        try:
            name : str = input()
            names.append(name)
        except EOFError:
            break

    if names:
        printNames(names)


if __name__ == "__main__":
    main()