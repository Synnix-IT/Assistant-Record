# implement a program that prompts the user for an arithmetic expression and
# then calculates and outputs the result as a floating-point value formatted to
# one decimal place.

def calculate():
    expression : str = input("Expression: ")

    result : float = float(eval(expression))        # Python 有內建的 eval() 函式來當計算機使用

    print(result)


if __name__ == "__main__":
    calculate()
