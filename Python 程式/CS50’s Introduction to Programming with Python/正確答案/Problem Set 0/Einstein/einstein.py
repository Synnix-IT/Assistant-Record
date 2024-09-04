# Calculate E = m * c^2

from math import pow


SPEED_OF_LIGHT : int = 300_000_000


# Mass-Energy Equivalence
def MEE(mass : int) -> int:

    return int(mass * pow(SPEED_OF_LIGHT, 2))


# Check input validity
def check(input : str) -> bool:

    return input.isdigit()


# Driver function
def main() -> None:
    mass = input()

    while True:
        if check(mass):
            print(MEE(int(mass)))
            break
        else:
            print("Invalid Input. Try again.")


if __name__ == "__main__":
    main()