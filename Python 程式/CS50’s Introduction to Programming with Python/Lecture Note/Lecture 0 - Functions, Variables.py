
def test() -> str:                                                         #使用物件導向詢問你叫啥，並輸入，回傳name以及x值
    name = input("What's your name? \n Your name:").strip().title()  #將以下功能合併
    name = name.strip()                                             #刪除空格
    name = name.capitalize()                                        #字首大寫
    name = name.title()                                             #每個單字首字大寫
    #first, last, end = name.split(" ")
    x = 123456
    return name

def test2() -> float:
    x = float(input("輸入數字1："))
    y = float(input("輸入數字2："))
    z = (x + y)
    return z

b= test()                                                      #設定nam, a為test執行結束的值

print(f"Hello, {b} ", sep="??????")                                         #打印出結果

a = test2()
print(f" {a:.2f} ")

