name = input("camelCase: ")

for c in name:
    if c.isupper() == True :
        print(f"_{c.lower()}", end = "")
    else:
        print(c, end = "")


