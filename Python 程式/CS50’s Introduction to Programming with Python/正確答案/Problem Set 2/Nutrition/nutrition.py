# Implement a program that prompts consumers users to input a fruit (case-insensitively) and
# then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits.

from typing import Final


FRUIT_TABLE : Final[dict[str, int]] = {

    "apple"             : 130   ,
    "avocado"           : 50    ,
    "banana"            : 110   ,
    "cantaloupe"        : 50    ,
    "grapefruit"        : 60    ,
    "grapes"            : 90    ,
    "honeydew melon"    : 50    ,
    "kiwifruit"         : 90    ,
    "lemon"             : 15    ,
    "lime"              : 20    ,
    "nectarine"         : 60    ,
    "orange"            : 80    ,
    "peach"             : 60    ,
    "pear"              : 100   ,
    "pineapple"         : 50    ,
    "plums"             : 70    ,
    "strawberries"      : 50    ,
    "sweet cherries"    : 100   ,
    "tangerine"         : 50    ,
    "watermelon"        : 80
}


def showCalories() -> None:
    fruit : str = input("Item: ").lower()

    if fruit in FRUIT_TABLE:
        print(f"Calories: {FRUIT_TABLE[fruit]}")


if __name__ == "__main__":
    showCalories()
