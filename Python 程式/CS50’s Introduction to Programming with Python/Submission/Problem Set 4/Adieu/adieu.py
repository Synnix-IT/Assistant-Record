import sys

def inputWord() -> str:                             #使用者輸入字串

    name = input("Name: ")
    return name

def printWord(list) -> None:                        #判斷打印的文字

    if len(list) <= 1:
        for word in list:
            print(f"Adieu, adieu, to {list[0]}")

    elif len(list) == 2:
        print("Adieu, adieu, to ", end = "")
        for word in list[:-1]:
            print(f"{word}", end = " ")
        print(f"and {list[-1]}")

    elif len(list) > 2:
        print("Adieu, adieu, to ", end = "")
        for word in list[:-1]:
            print(f"{word},", end = " ")
        print(f"and {list[-1]}")

def wordSave() -> list:                              #執行使用者輸入字串，如果偵測到 Control + D 則結束並打印
    word_list = []

    while True:

        try:
            word_list.append(inputWord())
        except EOFError:
            printWord(word_list)
            break

wordSave()
