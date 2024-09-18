import random
#import statistics
import sys
#import cowsay                                                                  #載入cowsay模組 (可以使其打印ASCII圖案)
import requests
#import json
import sayings

#print(random.randint(0, 5))                                                    #打印隨機0到5之間的整數
cards : list[int, str] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K", "A"]    #建立list (撲克牌)

random.shuffle(cards)                                                           #洗牌 (隨機打亂)

#for card in cards:                                                             #印出洗好的撲克牌
#    print(card)

#print(statistics.mean([100, 90]))                                              #平均分數

#if len(sys.argv) < 2:                                                           #檢查是否有輸入參數於執行程式後
#    sys.exit("Too few arguments")                                               #如果沒有則終止程式

#elif len(sys.argv) > 2:                                                        #檢查是否有輸入兩個以上參數
#    sys.exit("Too many arguments")                                             #如果有則終止程式

#for arg in sys.argv[1:]:                                                        
#    print("hello, my name is " + arg)

#print("hello, " + sys.argv[1])

#if len(sys.argv) == 2:
#    cowsay.trex("hello, " + sys.argv[1])

#if len(sys.argv) != 2:
#    sys.exit()

#response = requests.get("https://itunes.apple.com/search?entity=song&limit=10&term=" + sys.argv[1])
#print(json.dumps(response.json(), indent = 2)) 
#o = response.json()
#for result in o["results"]:
#    print(result["trackName"])

if len(sys.argv) == 2:
    
    sayings.goodbye(sys.argv[1])
    sayings.hello(sys.argv[1])