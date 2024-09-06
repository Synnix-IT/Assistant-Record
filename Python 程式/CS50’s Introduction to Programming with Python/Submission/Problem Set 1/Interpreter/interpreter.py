def inter():
    x, y, z = input("Expression: " ).strip().split(" ")

    if y == "/" and z == "0":
        inter()

    x, z = int(x), int(z)
    match y:
        case "+":
            print(float(x+z))
        case "-":
            print(float(x-z))
        case "*":
            print(float(x*z))
        case "/":
            print(float(x/z))


inter()
