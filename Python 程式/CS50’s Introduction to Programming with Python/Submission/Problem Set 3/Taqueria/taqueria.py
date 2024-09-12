taqueria : dict[str, int] = {

    "baja taco"         : 4.25  ,
    "burrito"           : 7.50  ,
    "bowl"              : 8.50  ,
    "nachos"            : 11.00 ,
    "quesadilla"        : 8.50  ,
    "super burrito"     : 8.50  ,
    "super quesadilla"  : 9.50  ,
    "taco"              : 3.00  ,
    "tortilla salad"    : 8.00
}

def input_food() -> str:

    food : str = input("Item: ").lower()
    return food

def calculate_price() -> int:
    total = 0
    while True:

        try:
            price = taqueria[input_food()]
            total = total + price
            print(f"Total: ${total:.2f}")
        except KeyError:
            pass
        except EOFError:
            break

calculate_price()
