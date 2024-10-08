
class Student:
    
    # def __init__(self, first, middle, last, house, patronus):             
    def __init__(self, name, house):                                        #將輸入的值標註類別 self 指的是自己。例如帶入 student = Student() 則自動指定 self = student
        #if not first:                                                      #檢查是否為空值
        #    raise ValueError("First name cannot be empty")

        #if not middle:
        #    raise ValueError("Middle name cannot be empty")
        
        #if not last:
        #    raise ValueError("Last name cannot be empty")
        
        #if house not in ["Stark", "Lannister", "Targaryen"]:               #檢查是否為合法值
        #    raise ValueError("Invalid house")                              #若不合法則報錯
        self.name = name                                                    #將輸入的值標註類別，以利後續使用
        self.house = house
        #self.patronus = patronus

    def __str__(self):                                                      #如果只有輸入 self 時的輸出
        return f"{self.name} from {self.house}"
    
    #def charm(self):                                                       #額外定義新函數於 class 內
    #    match self.patronus:
    #        case "Dragon":
    #            return "Fire"
    #        case "Phoenix":
    #            return "Air"
    #        case "Werewolf":
    #            return "Earth"
    #        case _:
    #            return "Unicorn"

def get_student():

    #student = Student()
    #student.name = input("Name: ")
    #student.house = input("House: ")

    #return student

    #student = {}                                                          #建立字典
    #student["name"] = input("Name: ")                                     #將輸入的值標註類別並存入字典
    #student["house"] = input("House: ")

    #return student

    #first = input("First Name: ")
    #middle = input("MiddleName: ")
    #last = input("Last Name: ")

    name = input("Name: ")
    house = input("House: ")
    #patronus = input("Patronus: ")
    student = Student(name, house)                                         #建立物件，帶入輸入的值
    #student = Student(first, middle, last, house, patronus)
 
    return student
    
    #return(name, house)                                                   #回傳值為元組，不可被修改
    #return [name, house]                                                  #回傳值為列表，可被修改


def main():
    
    student = get_student()
    #if student["name"] == "Padma":                                        #嘗試修改列表元素
    #    student["house"] = "Stark"
    print(student)                                                         #直接輸入 Self
    #print(f"{student.name} from {student.house}")
    #print(student.charm())


if __name__ == "__main__":
    main()

