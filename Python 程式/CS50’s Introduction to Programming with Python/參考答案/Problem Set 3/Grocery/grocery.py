# Implement a program that prompts the user for items, one per line, until the
# user inputs control-d (which is a common way of ending one’s input to a
# program).

# Then output the user’s grocery list in all uppercase, sorted alphabetically
# by item, prefixing each line with the number of times the user inputted that
# item.

# No need to pluralize the items.

# Treat the user’s input case-insensitively.


def main() -> None:
    grocery : dict[str, int] = dict()

    while True:
        try:
            item : str = input().upper()

            if item not in grocery:                 # 如果不存在於字典內
                grocery[item] = 1
            else:                                   # 如果存在則 + 1
                grocery[item] += 1

        except EOFError:                            # 用於抓取諸如 Ctrl + Z / Ctrl + D / Ctrl + C … 等終止指令
            break

    sorted_grocery = sorted(grocery.items())        # 排序字典

    for key, value in sorted_grocery:               # 印出排序後的字典
        print(f"{value} {key}")


if __name__ == "__main__":
    main()
