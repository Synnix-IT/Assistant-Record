# Implement a function called validate that expects an IPv4 address as input
# as a str and then returns True or False, respectively, if that input is a
# valid IPv4 address or not.


import re
import sys
from typing import Final


def validate(ip_address : str) -> bool:
    IP_FORMAT : Final[str] = r"^((25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    if re.search(IP_FORMAT, ip_address):
        return True

    return False


def main() -> None:
    ip_address : str = input("IPv4 Address: ")

    print(validate(ip_address))



if __name__ == "__main__":
    main()
