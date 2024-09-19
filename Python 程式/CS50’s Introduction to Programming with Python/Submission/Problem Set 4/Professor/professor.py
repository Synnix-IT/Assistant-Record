from random import randint

def main():
    level : int = get_level()                                                   #抓取使用者輸入的難度
    judge : int = 0                                                             #設定題目數量 (預設0)
    score : int = 10                                                            #紀錄分數 (預設10)
    wrong : int = 3                                                             #設定能錯誤的次數 (預設3)
    operate : bool = True                                                       #判斷是否要出新的題目
    while True:

        if operate:                                                             #判斷為 True 則出新題
            number_a, number_b = generate_integer(level)                        #隨機產生兩個數字

            operate = False

        answer : str = input(f"{number_a} + {number_b} = ")                     #打印題目並請使用者輸入

        if not answer.isdigit():                                                #如果輸入非數字
            print("EEE")                                                        #打印 EEE

        elif int(answer) != (number_a + number_b):                              #如果輸入數字與答案不符
            print("EEE")                                                        #打印 EEE
            wrong -= 1                                                          #錯誤次數 -1

        else:
            judge  += 1                                                         #如果答對，題數 +1
            wrong   = 3                                                         #重製錯誤次數
            operate = True                                                      #繼續出新題目

        if wrong == 0:                                                          #如果錯誤次數歸零
            print(f"{number_a} + {number_b} = {number_a + number_b}")           #打印答案
            wrong   = 3                                                         #重製錯誤次數
            operate = True                                                      #出新題目
            score  -= 1                                                         #分數 -1
            judge  += 1                                                         #題目 +1

        if judge == 10:                                                         #如果到達10題
            print(f"Score: {score}")                                            #打印分數
            break

def get_level() -> int:
    while True:

        input_level = input("Level: ")                                          #請使用者輸入難度

        if input_level.isdigit() and 1 <= int(input_level) <= 3:                #判斷使用者輸入
            return int(input_level)

def generate_integer(level) -> int:

    if level == 1:                                                              #難度 1
        number_a : int = randint(0, 10)
        number_b : int = randint(0, 10)

    elif level == 2:                                                            #難度 2
        number_a : int = randint(10, 99)
        number_b : int = randint(10, 99)

    elif level == 3:                                                            #難度 3
        number_a : int = randint(100, 999)
        number_b : int = randint(100, 999)

    return number_a, number_b


if __name__ == "__main__":
    main()
