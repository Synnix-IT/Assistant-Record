def main():
    x = input("What time is it?" )

    y = convert(x)

    if 7 <= y <= 8:
        print("breakfast time")
    elif 12 <= y <= 13:
        print("lunch time")
    elif 18 <= y <= 19:
        print("dinner time")
    else:
        pass

def convert(time : str) -> float :
    tlist = time.split(":")

    h, m = float(tlist[0]), float(tlist[-1])

    t = h+(m/60)

    return t

if __name__ == "__main__":
    main()
