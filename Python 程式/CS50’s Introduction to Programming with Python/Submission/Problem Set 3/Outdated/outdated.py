delete = str.maketrans({"," : "", "/" : " "})                                           #建議要替代的字串
change : dict[str, int]= {                                                              #建立月份字典
    "January"   :   1,
    "February"  :   2,
    "March"     :   3,
    "April"     :   4,
    "May"       :   5,
    "June"      :   6,
    "July"      :   7,
    "August"    :   8,
    "September" :   9,
    "October"   :   10,
    "November"  :   11,
    "December"  :   12
}
def dictionary() -> int:
    while True:

        date_input : str = input("Date: ").strip()                                      #定義使用者輸入日期並去掉左右空格

        if "," in date_input:                                                           #如果輸入字串含[,]
            date_list : list = date_input.translate(delete).split(" ")                  #整理字串並分類為list

            try:
                date_list[0] = change[date_list[0]]                                     #嘗試替代月份字串為數字
            except KeyError:
                pass

        elif "/" in date_input:                                                         #如果輸入字串含[/]
            date_list : list = date_input.split("/")                                    #整理字串並分類為list

        elif " " in date_input:                                                         #如果輸入字串含[ ]
            date_list : list = date_input.split(" ")                                    #整理字串並分類為list

        try:
            mouth, date, year= int(date_list[0]), int(date_list[1]), int(date_list[2])  #將分類結果轉換為數字
            return mouth, date, year
        except ValueError:
            pass

def judge() -> None:
    while True:

        mouth, date, year = dictionary()

        if  0 < mouth < 13 and  0 < date < 31:                                          #判斷日期的合理性
            print(f"{year}-{mouth:0>2d}-{date:0>2d}")                                   #打印結果
            break
        else:
            pass

judge()
