def main():
    value(input("Greeting: "))

def value(greeting):
    delete = str.maketrans({"," : "", "!" : "", "." : ""})

    text = greeting.translate(delete).lower()

    word = text.split()

    if word[0] in "hello":
        money = 0
        return money

    elif text[0] == "h":
        money = 20
        return money

    else:
        money = 100
        return money


if __name__ == "__main__":
    main()
