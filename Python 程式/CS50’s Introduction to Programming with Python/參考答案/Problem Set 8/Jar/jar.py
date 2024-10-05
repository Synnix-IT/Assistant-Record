# implement a class called Jar with these methods:

# __init__ should initialize a cookie jar with the given capacity, which represents the maximum number of cookies that
# can fit in the cookie jar. If capacity is not a non-negative int, though, __init__ should instead raise a ValueError.

# __str__ should return a str with 🍪, where is the number of cookies in the cookie jar. For instance, if there are 3
# cookies in the cookie jar, then str should return "🍪🍪🍪"

# deposit() should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though,
# deposit() should instead raise a ValueError.

# withdraw() should remove n cookies from the cookie jar. Nom nom nom. If there aren’t that many cookies in the cookie
# jar, though, withdraw should instead raise a ValueError.

# capacity() should return the cookie jar’s capacity.

# size() should return the number of cookies actually in the cookie jar, initially 0.


class Jar:
    def __init__(self, capacity : int = 12) -> None:
        if capacity < 0:
            raise ValueError("Capacity cannot be negative")

        self.__capacity : int = capacity
        self.__size     : int = 0


    def __str__(self) -> str:
        return "🍪" * self.__size


    def deposit(self, amount : int) -> None:
        if (self.__size + amount) > self.__capacity:
            raise ValueError("Exceed capacity")

        self.__size += amount


    def withdraw(self, amount : int) -> None:
        if self.__size - amount < 0:
            raise ValueError("Not enough cookies in the jar")

        self.__size -= amount


    @property
    def capacity(self) -> int:
        return self.__capacity


    @property
    def size(self) -> int:
        return self.__size


def main():
    jar = Jar()

    jar.deposit(5)
    jar.withdraw(2)

    print(jar.capacity)
    print(jar.size)


if __name__ == "__main__":
    main()