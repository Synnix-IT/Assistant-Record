class Jar:
    def __init__(self, capacity = 12):

        self._capacity = capacity
        self._size = 0

        if capacity < 0:
            raise ValueError


    def __str__(self):

        return "🍪" * self._size


    def deposit(self, cookie):
        if (self._size + cookie) > self._capacity:
            raise ValueError

        self._size += cookie


    def withdraw(self, cookie):
        if (self._size - cookie) < 0:
            raise ValueError

        self._size -= cookie

    @property
    def capacity(self):

        return self._capacity

    @property
    def size(self):
        return self._size


def main():

    jar = Jar()

    jar.deposit(5)
    jar.withdraw(3)

    print(jar.capacity)
    print(jar.size)
    print(jar)

if __name__ == "__main__":
    main()
