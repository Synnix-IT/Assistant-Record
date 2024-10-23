def sheep(n):
    for i in range(n):
        yield "🐑" * i                  #利用 yield 個別生成，以免佔據記憶體


def main():
    n = int(input("What's n?"))

    for s in sheep(n):
        print(s)


if __name__ == "__main__":
    main()