# Implement a program that prompts the user to insert a coin, one at a time,
# each time informing the user of the amount due. Once the user has inputted
# at least 50 cents, output how many cents in change the user is owed.

from typing import Final

ACCEPTED_COIN : Final[list[int]] = [5, 10, 25]

def sellCoke() -> None:
    coke : int = 50

    while True:
        print(f"Amount Due: {coke}")

        coin : int = int(input("Insert Coin: "))

        if coin in ACCEPTED_COIN:
            coke -= coin

        if coke <= 0:
            print(f"Change Owned: {abs(coke)}")
            break


if __name__ == "__main__":
    sellCoke()
