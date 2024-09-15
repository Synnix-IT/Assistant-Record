food_list = []                            #建立list

while True:
    try:
        food_list.append(input().upper()) #請使用者輸入東西並全大寫寫入list

    except EOFError:                      #偵測按鍵結束迴圈
        break

food_list.sort()                          #排序list
for item in food_list:

    print(food_list.count(item), item)    #打印東西輸入次數，打印東西名稱
    food_list.remove(item)                #刪除打印過的東西

