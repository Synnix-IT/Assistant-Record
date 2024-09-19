import sys
import requests


if len(sys.argv) < 2:                                                                       #判斷執行程式後沒有輸入文字
    sys.exit("Missing command-line argument")

elif sys.argv[1].isalpha():                                                                 #判斷在執行程式後輸入英文
    sys.exit("Command line argument is not a number")

else:
    response : str = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")      #抓取比特幣價格.json檔案
    btc : float = float(response.json()["bpi"]["USD"]["rate"].replace(",", ""))             #指定抓取比特幣 (美金) 價格
    print(f"${float(sys.argv[1]) * btc :,}", end = "")                                      #換算使用者有的數量，並補上千位符號
