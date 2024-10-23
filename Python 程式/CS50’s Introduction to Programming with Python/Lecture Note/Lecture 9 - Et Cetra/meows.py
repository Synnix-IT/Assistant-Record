class Cat:
    def __init__(self, number : int) -> None:
        self._number : int = number


    @property
    def number(self):
        return self._number
    

    def __str__(self) -> str:
        return "meow\n" * self._number


def main() -> None:

    cat : Cat = Cat(int(input("Number: ")))
    print(cat, end = "")

if __name__ == "__main__":
    main()