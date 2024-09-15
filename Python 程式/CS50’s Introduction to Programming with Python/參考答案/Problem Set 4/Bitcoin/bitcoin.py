# Implement a program that:

#   Expects the user to specify as a command-line argument the number of
#   Bitcoins that they would like to buy. If that argument cannot be converted
#   to a float, the program should exit via sys.exit with an error message.

#   Queries the API for the CoinDesk Bitcoin Price Index at
#   https://api.coindesk.com/v1/bpi/currentprice.json, which returns a JSON object,
#   among whose nested keys is the current price of Bitcoin as a float.

import requests
import sys


def checkArguments(arguments : list[str]) -> bool:
    if len(arguments) != 2:
        sys.exit("Missing command-line argument")

    try:
        number : float = float(arguments[1])
    except ValueError:
        sys.exit("Command-line argument is not a number")


def getCoinPrice(number : float) -> float:
    data : requests.Response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

    price = data.json()["bpi"]["USD"]["rate_float"]

    return float(price) * number



def printPrice(price : float) -> None:
    print(f"${price:,.4f}")


def main() -> None:
    checkArguments(sys.argv)

    price : float = getCoinPrice(float(sys.argv[1]))

    printPrice(price)


if __name__ == "__main__":
    main()
