def main():
    shorten()


def shorten(word):
    delete : list[str] = ["a","e","i","o","u"]

    for c in word:
        if c.lower() in delete :
            word = word.replace(c, "")

    return word

if __name__ == "__main__":
    main()



