def checkInput(input : str) -> bool:
    """
    Check if the input string is a digit.

    Parameters
    ----------
    input : str
        The string to check.

    Returns
    -------
    bool
        True if the string is a digit, False otherwise.
    """

    return input.isdigit()                                                                  # 檢查輸入是否為數字，是則回傳 True，否則回傳 False

def getInput() -> tuple:
    """
    Get the input from user, including minimum, maximum, and the number of times to guess.

    Returns
    -------
    tuple
        A tuple of three elements, including minimum, maximum, and the number of times to guess.
    """

    while True:
        min = input("請輸入最小值: ")
        if checkInput(min):
            min = int(min)
            break
        else:
            print("請輸入數字")

    while True:
        max = input("請輸入最大值: ")
        if checkInput(max):
            max = int(max)
            break
        else:
            print("請輸入數字")

    while True:
        times = input("請輸入猜測次數: ")

        if checkInput(times):
            times = int(times)
            break
        else:
            print("請輸入數字")

    return min, max, times                                                                  # 回傳一個 tuple，包含最小值、最大值、猜測次數