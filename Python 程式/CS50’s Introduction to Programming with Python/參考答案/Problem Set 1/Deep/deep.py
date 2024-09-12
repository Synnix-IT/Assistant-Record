# Implement a program that prompts the user for the answer to the Great Question of Life,
# the Universe and Everything, outputting Yes if the user inputs 42 or
# (case-insensitively) forty-two or forty two. Otherwise output No
from typing import Union

# Requirement
def deep() -> None:
    line : str = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")

    answer : list[Union[int, str]] = ["42", "forty-two", "forty two"]                                               # 將可接受的答案先記錄在一個 List 內

    if line.lower().strip() in answer:                                                                              # 刪掉左右空格，轉換成小寫後再判斷
        print("Yes")
    else:
        print("No")


# Driver Code
if __name__ == "__main__":
    deep()
