import sys
import csv


if len(sys.argv) < 2 :                                                                                      #偵測執行命令時無傳入參數 (檔案) 則報錯
    sys.exit("Too few command-line arguments")

if 3 < len(sys.argv):                                                                                       #偵測執行命令時傳入參數 (檔案) 過長則報錯
    sys.exit("Too many command-line arguments")

if ".csv" not in sys.argv[1]:                                                                               #偵測執行命令時傳入參數 (檔案) 不為 csv 檔案則報錯
    sys.exit("Not a CSV file")


for word in sys.argv[1:]:                                                                                   #開啟檔案
    try:
        with open (sys.argv[1]) as read, open (sys.argv[2], 'w', newline = '') as write:                    #讀取檔案 & 寫入檔案

            reads = csv.DictReader(read)                                                                    #讀取檔案

            writer = csv.DictWriter(write, fieldnames = ["first", "last", "house"])                         #寫入檔案並定義標題
            writer.writeheader()                                                                            #製作標題

            for row in reads:                                                                               #讀取並分配資料
                last, first = row["name"].replace(" ","").split(",")                                        #將資料分割為 first & last
                
                writer.writerow({"first" : first, "last" : last, "house" : row["house"]})                   #寫入檔案，first & last & house


    except FileNotFoundError:                                                                               #檔案不存在則報錯
        sys.exit(f"Could not read {word}")

