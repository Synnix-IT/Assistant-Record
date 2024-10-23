class Bank:
    def __init__(self):
        self._balance = 0

    @property
    def balance(self):
        return self._balance
    
    def deposit(self, amount):
        self._balance += amount

    def withdraw(self, amount):
        self._balance -= amount

def main():
    
    bank = Bank()
    bank.deposit(1000)
    bank.withdraw(500)

    print(f"Balance: {bank.balance}")

if __name__ == "__main__":
    main()