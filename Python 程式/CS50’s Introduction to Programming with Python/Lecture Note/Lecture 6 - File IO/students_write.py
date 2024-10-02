import csv

name = input("What's your name? ")
gender = input("What's your gender? ")
number = input("What's your number? ")

with open("students3.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "gender", "number"])
    writer.writerow({"name" : name, "gender" : gender, "number" : number}) 