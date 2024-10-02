import csv

students : list[dict] = []                                                              #建立空串列

with open("students.csv") as file:                                                      #開啟檔案

    reader : str = csv.DictReader(file)                                                 #讀取檔案
    
    for line in sorted(file):                                                           #將檔案內容排序並轉化為字典

        name, gender, number = line.rstrip().split(",")                                 #將檔案內容轉換為字典，以","分隔

        #print(f"{name} is {gender}.")                                                  
        #students.append(f"{name} is {gender}.")
        student = {"name": name, "gender": gender, "number" : number}                   #設定字典格式，並將檔案內容轉換為字典
        #student["name"] = name
        #student["gender"] = gender
        students.append(student)                                                        #將字典內容加入串列


def get_name(student : dict) -> str:
    return student["name"]

def get_gender(student : dict) -> str:
    return student["gender"]


def get_number(student : dict) -> str:
    return student["number"]


for student in sorted(students, key=get_name, reverse = False):                             #排序 : key = 依照的是哪個欄位 ; reverse = 是否為反向排序 (預設為 False) 
    print(f"{student["name"]} is a {student["gender"]}, number is {student["number"]}" )

#print(students)