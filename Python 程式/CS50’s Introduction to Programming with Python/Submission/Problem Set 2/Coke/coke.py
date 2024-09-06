coke = 50

def prco(c):
    print(f"Amount Due: {c}")

while True:
    prco(coke)
    buy = int(input("Insert Coin: "))

    if buy == 25 or buy == 10 or buy == 5:
        coke = coke - buy
        if coke <= 0:
            print(f"Change Owed: {abs(coke)}")
            break


