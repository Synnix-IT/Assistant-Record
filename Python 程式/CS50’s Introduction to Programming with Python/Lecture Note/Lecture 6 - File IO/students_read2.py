import csv

students : list[dict] = []                                                                                  #建立空串列

with open("students2.csv") as file:                                                                          #開啟檔案

    reader : str = csv.DictReader(file)                                                                     #讀取檔案
    
    for row in reader:                                                                                      #將檔案內容轉換為字典
        students.append({"name" : row["name"] , "gender" : row["gender"] , "number" : row["number"]})

for student in sorted(students, key=lambda student: student["name"], reverse = False):                      #將字典內容按照特定欄位字母順序排序，以 lambda 用於代替 def 並設定排序依據
    print(f"{student["name"]} is a {student["gender"]}, number is {student["number"]}" )
