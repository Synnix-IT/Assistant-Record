#names = []

#for _ in range(3):

#    names.append(input("What's your name?"))

#for name in sorted(names):
#    print(f"hello, {name}")

#name = input("What's your name? ")

#file = open("names.txt", "a")                          #開啟檔案並寫入，a為append，可以使原本的檔案內容不被替換
#with open("names.txt", "a") as file:                    #用於避免開啟檔案時出現問題 (忘記寫入 close)
#    file.write(f"{name}, \n")
#file.close()

#with open("names.txt", "r") as file:

#    for line in file:
#        print(f"Hello, {line.rstrip()}")

names = []

with open("names.txt") as file:
    for line in sorted(file):                           #將檔案內容按照字母順序排序
        names.append(line.rstrip())
  
for name in sorted(names, reverse=True):                #將檔案內容按照字母倒序排序
    print(f"hello, {name}")