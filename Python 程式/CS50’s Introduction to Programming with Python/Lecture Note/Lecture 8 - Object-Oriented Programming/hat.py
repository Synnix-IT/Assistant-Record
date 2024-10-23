import random

class Hat:

    def __init__(self) -> None:
        self.houses :list = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]


    def sort(self, name):
        house : str = random.choice(self.houses)
        print(f"{name} is in some {house}.")

hat = Hat()
hat.sort("Harry")