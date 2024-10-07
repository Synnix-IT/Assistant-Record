import sys

if len(sys.argv) < 2 :                                                          #偵測執行命令時無傳入參數 (檔案) 則報錯
    sys.exit("Too few command-line arguments")

if 2 < len(sys.argv):                                                           #偵測執行命令時傳入參數 (檔案) 過長則報錯
    sys.exit("Too many command-line arguments")

if ".py" not in sys.argv[1]:                                                    #偵測執行命令時傳入參數 (檔案) 不為 python 檔案則報錯
    sys.exit("Not a Python file")

for word in sys.argv[1:]:
    try:
        with open (word, "r") as r:                                             #開啟檔案

            reads = r.readlines()
            line = 0

            for space in reads:                                                 #讀取檔案每一行
                space = space.strip()                                           #將讀取的文字去除空白
                if not space or space.startswith("#") or space == "\n":         #檢查是否為空白、註解、換行符號
                    line += 1                                                   #計算空白、註解行數
                    
        print(len(reads) - line, end = "")                                      #將行數減去空白、註解行數後印出

    except FileNotFoundError:                                                   #檔案不存在則報錯
        sys.exit("File does not exist")


