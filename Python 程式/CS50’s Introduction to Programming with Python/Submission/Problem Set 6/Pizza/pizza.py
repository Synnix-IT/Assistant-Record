import sys
import csv
from tabulate import tabulate                                                                                   #使用tabulate (輸出字符表格) 套件

foods : list[dict] = []                                                                                         #建立總食物清單空字典
table_header = []                                                                                               #建立表格標題
table_data = []                                                                                                 #建立表格資料

if len(sys.argv) < 2 :                                                                                          #偵測執行命令時無傳入參數 (檔案) 則報錯
    sys.exit("Too few command-line arguments")

if 2 < len(sys.argv):                                                                                           #偵測執行命令時傳入參數 (檔案) 過長則報錯
    sys.exit("Too many command-line arguments")

if ".csv" not in sys.argv[1]:                                                                                   #偵測執行命令時傳入參數 (檔案) 不為 csv 檔案則報錯
    sys.exit("Not a CSV file")


for word in sys.argv[1:]:                                                                                       #開啟檔案
    try:
        with open (word) as r:

            reads = csv.DictReader(r)                                                                           #讀取檔案每一行
            storeName , fileName = sys.argv[1].split(".")                                                       #取得檔案名稱
            storeName = (storeName.capitalize() + " Pizza")                                                     #製作專屬標題

            for row in reads:                                                                                   #讀取並分配資料 (以字典形式)
                foods.append({storeName : row[storeName] , "Small" : row["Small"] , "Large" : row["Large"]})    #將資料加入總食物清單
        
        table_header = [storeName, "Small", "Large"]                                                            #製作表格標題

        for food in (foods):

            table_data.append([food[storeName], food["Small"], food["Large"]])                                  #製作表格資料

        print(tabulate(table_data, headers=table_header, tablefmt='grid'))                                      #繪製表格

    except FileNotFoundError:                                                                                    #檔案不存在則報錯
        sys.exit("File does not exist")
