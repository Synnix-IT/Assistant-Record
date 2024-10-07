import sys
from PIL import Image, ImageOps                                 #導入函式庫

if len(sys.argv) < 3 :                                          #偵測執行命令時傳入參數 (檔案) 過短則報錯
    sys.exit("Too few command-line arguments")

if 3 < len(sys.argv):                                           #偵測執行命令時傳入參數 (檔案) 過長則報錯
    sys.exit("Too many command-line arguments")

if "." not in sys.argv[1]:                                      #偵測執行命令時傳入參數 (檔案) 不為檔案則報錯
    sys.exit("Invalid input")

name1, file1 = sys.argv[1].split(".")                           #分割檔名及副檔名
name2, file2 = sys.argv[2].split(".")

if not file1 == file2:                                          #如副檔名不相同則報錯
    sys.exit("Input and output have different extensions")

try:                                                            #嘗試開啟檔案 (如無檔案則退出)
    img1 = Image.open(sys.argv[1])                              #開啟檔案
    imgShirt = Image.open("shirt.png")                          #開啟預設衣服檔案
    imgSize = imgShirt.size                                     #設定要裁切的大小 = 衣服大小
    result = Image.new(img1.mode, (imgSize))                    #建立要貼上的照片
    img1 = ImageOps.fit(img1, imgSize)                          #裁切照片
    result.paste(img1,(0, 0))                                   #先貼上原照片
    result.paste(imgShirt,(0, 0),imgShirt)                      #貼上並去背衣服照片
    result.save(sys.argv[2])                                    #儲存照片

except FileNotFoundError:                                       #開啟檔案失敗退出並顯示訊息
    sys.exit("Input does not exist")

