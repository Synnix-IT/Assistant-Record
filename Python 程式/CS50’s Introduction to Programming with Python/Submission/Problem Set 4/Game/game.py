from random import randint

def numberRange(max : int) -> int:                                  #取亂數 (整數) 作為答案

    answer : int = randint(1, max)
    return int(answer)

def inputLevel() -> int:                                            #判斷輸入最大值為正整數
    while True:

        input_level : str = input("Level: ")

        if input_level.isdigit() and int(input_level) > 0 :
           answer : int = numberRange(int(input_level))
           return answer

def inputNumber() -> int:                                           #判斷輸入猜的數為正整數
    while True:

        input_number : str = input("Guess: ")

        if input_number.isdigit() and int(input_number) > 0:
           return int(input_number)

def judge():                                                        #判斷並執行是否正確，正確結束，否則提示並繼續

    answer : int = inputLevel()
    guess : int = inputNumber()

    while True:

        if answer > guess:
            print("Too small!")
            guess : int = inputNumber()

        if answer == guess:
            print("Just right!")
            break
        if answer < guess:
            print("Too large!")
            guess : int = inputNumber()

judge()

