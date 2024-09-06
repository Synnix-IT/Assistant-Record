def test(a, b: str) -> int:
    a, b = int(a), int(b)
    if a < b:
        print("第一個數字小於第二個數字")
    elif a > b:
        print("第一個數字大於第二個數字")
    elif a == b:
        print("第一個數字等於第二個數字")

    if a != b :
        print("兩個數字不相等")
def judge(a: str) -> bool:
    a = int(a)
    return a % 2 == 1
    #return ("偶數") if a % 2 == 0 else ("奇數")

def ask() -> str:
    x = input("請輸入第一個數字：")
    y = input("請輸入第二個數字：")
    test(x, y)
    print(judge(x))

def asknumber() -> str:
    z = input("請輸入數字(0~3)： ")
    match z:
        case "0":
            print(f"你輸入了 零 ")
        case "1":
            print(f"你輸入了 一 ")
        case "2":
            print(f"你輸入了 二 ")
        case "3":
            print(f"你輸入了 三 ")
        case _:
            print("超出範圍，請重新輸入")
            asknumber()
        

#ask()
asknumber()