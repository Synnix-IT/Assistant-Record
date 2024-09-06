delete = ["a","e","i","o","u"]
name = input("Input: ")

for c in name:
    if c.lower() in delete :
        pass
    else:
        print(c, end = "")


