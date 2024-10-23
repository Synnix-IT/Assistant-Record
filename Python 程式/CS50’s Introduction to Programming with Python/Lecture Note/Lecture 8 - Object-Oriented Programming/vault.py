class Vault:
    def __init__(self, galleons = 0, sickles = 0, knuts = 0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

    def __str__(self):
        return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"
    
    def __add__(self, other):                           #建立加法運算子，將兩個輸入的錢加起來
        galleons = self.galleons + other.galleons
        sickles = self.sickles + other.sickles
        knuts = self.knuts + other.knuts
        return Vault(galleons, sickles, knuts)
    
potter = Vault(100, 50, 20)

print(potter)

weasley = Vault(20, 50, 100)

print(weasley)

total = potter + weasley

print(total)