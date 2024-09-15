# Implement a program that:

#   Prompts the user for a level, n. If the user does not input a positive
#   integer, the program should prompt again.

#   Randomly generates an integer between 1 and n inclusive, using the random
#   module.

#   Prompts the user to guess that integer. If the guess is not a positive
#   integer, the program should prompt the user again.

#   If the guess is smaller than that integer, the program should output Too
#   small! and prompt the user again.

#   If the guess is larger than that integer, the program should output Too
#   large! and prompt the user again.

#   If the guess is the same as that integer, the program should output Just
#   right! and exit.

from random import randint

def getNumber() -> int:
    while True:
        number : str = input("Level: ")

        if number.isdigit() and int(number) > 0:
            break

    return randint(1, int(number))


def main() -> None:
    answer : int = getNumber()

    while True:
        guess : str = input("Guess: ")

        if not guess.isdigit():
            continue

        guess = int(guess)

        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        elif guess == answer:
            print("Just right!")
            break


if __name__ == "__main__":
    main()