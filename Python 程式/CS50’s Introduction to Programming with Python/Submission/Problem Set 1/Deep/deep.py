def judge() -> str:
    number = input("input：").lower().replace(" " , "")
    condition = ["42", "fortytwo", "forty-two"]
    if number in condition :
        print("Yes")
    else:
        print("No")
judge()
