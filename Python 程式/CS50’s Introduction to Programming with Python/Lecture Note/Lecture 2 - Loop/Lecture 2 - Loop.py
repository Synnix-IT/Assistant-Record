def wloop(i : int):                                   

        while i != 0:                                   #建立while迴圈，條件:當i不等於0時
            print("meow")                               #印出meow      
            i -= 1                                      #i減1

#wloop(3)

def floop(x : int):                                     
    
        for i in range(x):                              #建立for迴圈，條件:當i不等於x時
            print(f"meow {i+1} ")                       #印出meow i+1次

def judge() -> int:                                     
        while True:

            a = input("pleace input a number : ")       #請輸入數字                

            if a.isdigit() == True:                     #判斷是否為數字
                return int(a)                           #回傳數字
            else:
                print("input again")                    #輸入錯誤則重新輸入
        
def students():                                         
    
        stu = ["jeorge" , "bob" , "james" , "jacy"]     #建立名字串列

        for student in stu:                             #建立for迴圈
            print(student)                              #印出名字

def students2():                                        
    
        stu = ["jeorge" , "bob" , "james" , "jacy"]     #建立名字串列

        for i in range(len(stu)):                       #建立for迴圈
            print(i + 1, stu[i])                        #印出順序及名字

def students3():
    
        stu = {                                         #建立字典
            "jeorge" : "boy", 
            "bob" : "boy",
            "james" : "girl",
            "jacy" : "girl",
            }
        
        for i in stu:                                   #建立for迴圈
            print(i, stu[i] , sep = ", ")               #印出名字及性別
def students4():
    
        stu = [                                                            #建立字典   
            {"name" : "jeorge" , "sex" : "boy" , "age" : 18},
            {"name" : "bob" , "sex" : "boy" , "age" : 21},
            {"name" : "james" , "sex" : "girl" , "age" : 17},
            {"name" : "jacy" , "sex" : "girl" , "age" : 19},
            {"name" : "jack" , "sex" : "boy" , "age" : 23},
        ] 
        for i in stu:                                                       
            print(i["name"], i["sex"], i["age"], sep = ", ")                #印出名字、性別、年齡
    
def mario():
        print_column(4)

def print_column(h : int):

        for _ in range(h):
            print("#" * h)

#mario()

#students4()

#floop(judge())

#print("meow\n" * 3 , end = "")