import re

def parse(s) -> str:

    url = re.search(r"(?:<iframe src=\")(?:https?://)?(?:www\.)?youtube.com/(?:\w+)?/(\w+)", s, re.IGNORECASE)              #使用正則表達式驗證 youtube 網址

    if url.group(1) == None:                                                                                                #分割結果為 None 時，回傳 None
        return url.group(1)
    else:                                                                                                                   #分割結果不為 None 時，回傳網址
        return(f"https://youtu.be/{url.group(1)}")

def main():
    print(parse(input("HTML: ").strip()))


if __name__ == "__main__":
    main()
