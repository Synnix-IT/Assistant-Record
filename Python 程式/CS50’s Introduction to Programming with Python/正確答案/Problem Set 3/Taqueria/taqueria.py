# Implement a program that enables a user to place an order, prompting them
# for items, one per line, until the user inputs control-d (which is a common
# way of ending one’s input to a program).
#
# After each inputted item, display the total cost of all items inputted thus
# far, prefixed with a dollar sign ($) and formatted to two decimal places.
# Treat the user’s input case insensitively.

from typing import Final

MENU : Final[dict[str, int]] = {

    "Baja Taco"         : 4.25  ,
    "Burrito"           : 7.50  ,
    "Bowl"              : 8.50  ,
    "Nachos"            : 11.00 ,
    "Quesadilla"        : 8.50  ,
    "Super Burrito"     : 8.50  ,
    "Super Quesadilla"  : 9.50  ,
    "Taco"              : 3.00  ,
    "Tortilla Salad"    : 8.00
}


def main() -> None:
    order_list: list[float] = []                            # 用於儲存已經點過的餐

    while True:
        try:
            order = input("Item: ").title()

            if order in MENU:
                order_list.append(MENU[order])

                print(f"Total: ${sum(order_list):.2f}")

        except EOFError:                                    # 用於抓取諸如 Ctrl + Z / Ctrl + D / Ctrl + C … 等終止指令
            break


if __name__ == "__main__":
    main()