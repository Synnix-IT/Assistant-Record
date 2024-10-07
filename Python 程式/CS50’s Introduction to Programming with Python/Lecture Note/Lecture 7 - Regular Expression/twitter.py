import re

url = input("URL: ").strip()

#username = url.replace("https://twitter.com/" , "")

#username = re.sub (r"(https?://)?(www\.)?twitter.com/", "", url)                            #使用正則表達式 sub 替換

if matches := re.fullmatch(r"(?:https?://)?(?:www\.)?twitter.com/(.+)", url, re.IGNORECASE):   #?:代表在做 group 時不要匹配，例如: (https?://)?
    print(f"Username: {matches.group(1)}")

