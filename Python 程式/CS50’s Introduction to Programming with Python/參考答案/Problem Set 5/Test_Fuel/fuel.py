# Implement a program that prompts the user for a fraction, formatted as X/Y,
# wherein each of X and Y is an integer, and then outputs, as a percentage
# rounded to the nearest integer, how much fuel is in the tank.

# If, though, 1% or less remains, output E instead to indicate that the tank
# is essentially empty. And if 99% or more remains, output F instead to
# indicate that the tank is essentially full.


def convert(fraction : str) -> int:
    while True:
        try:
            if "." in fraction:                                         # 分子或分母不能是浮點數，用 . 判斷是否為小數
                raise ValueError                                        # 如為浮點數則報錯，此函式停止

            numerator : int = None                                      # 如有宣告一個變數，一定要給值，如果暫時沒值就給 None
            denominator : int = None
            numerator, denominator = map(int, fraction.split("/"))      # map(<function>, <Iterable>)，對可迭代後者所有值進行 <function> 函式
                                                                        # 進行完函式，分配給變數

            if denominator == 0:
                raise ZeroDivisionError                                 # 分母不可為 0，如為 0 則報錯，此函式停止

            result : float = numerator / denominator

            if not 0 <= result <= 1:                                    # 值必須在 0 和 1 之間，如超過範圍則報錯，此函式停止
                raise ValueError

            return int(round(result, 2) * 100)

        except (ValueError, ZeroDivisionError):                         # 如有遇到報錯，截獲報錯，從此處開始執行
            continue


def gauge(current_fuel : int) -> str:
    if current_fuel >= 99:
        return "F"
    elif current_fuel <= 1:
        return "E"
    else:
        return f"{int(round((current_fuel)))}%"                   # round() 會回傳該浮點數最近之整數



def main() -> None:
    fraction : str = input("Fraction: ")

    current_fuel : int = convert(fraction)

    print(gauge(current_fuel))


if __name__ == "__main__":
    main()
