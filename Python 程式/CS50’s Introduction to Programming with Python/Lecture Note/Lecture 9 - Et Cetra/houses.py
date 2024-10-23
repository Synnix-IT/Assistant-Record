students : dict = [
    {"name": "Harry", "house": "Gryffindor"},
    {"name": "Hermione", "house": "Gryffindor"},
    {"name": "Ron", "house": "Gryffindor"},
    {"name": "Draco", "house": "Slytherin"},
    {"name": "Padma", "house": "Ravenclaw"},
]

#houses = []
houses : set = set()
for student in students:
        houses.add(student["house"])                        #使用 Set 代替 List
#    if student["house"] not in houses:
#        houses.append(student["house"])

for house in sorted(houses):
    print(house)
