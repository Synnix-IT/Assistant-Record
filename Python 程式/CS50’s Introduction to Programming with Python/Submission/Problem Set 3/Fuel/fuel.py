def int_input() -> int:
    while True:

        try:
            x, y= input("Fraction: ").split("/")
            numerator : int = int(x)
            denominator : int= int(y)
            return numerator, denominator
        except ValueError:
            pass

def calculate() -> int:
    while True:

        try:
            numerator, denuminator = int_input()
            result : int = int(round(numerator/denuminator*100))
            return result
        except ZeroDivisionError:
            pass

def judge():
    while True:

        value : int = calculate()

        if value > 100:
            pass

        elif 100 >= value >= 99:
            print("F")
            break
        elif value <= 1:
            print("E")
            break
        else:
            print(f"{value}%")
            break

def main():

    judge()

main()
