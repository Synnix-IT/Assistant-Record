import re

name = input("What's your name? ").strip()               #使用者輸入後先去空格



if matches := re.fullmatch(r"(.+), *(.+)", name):        #設定正則表達式，以便後續使用
    #last, first = matches.groups()                      #將表達式分割為 last & first; .groups() 可以取得正則表達式的所有分割結果
    
    #last = matches.group(1)                             #將表達式分割為 last & first
    #first = matches.group(2)
    #name = f"{first} {last}"                            #將 last & first 合併

    name = f"{matches.group(2)} {matches.group(1)}"
print(f"hello, {name}")