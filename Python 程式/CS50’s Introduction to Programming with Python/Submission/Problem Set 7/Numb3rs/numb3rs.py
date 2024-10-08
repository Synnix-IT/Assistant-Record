import re

def main() -> None:
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip : str) -> bool:
    if ip := re.search(r"^((1?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])\.){3}(1?[0-9]?[0-9]|2[0-4][0-9]|25[0-5])$", ip):         #使用正則表達式驗證 IPv4 (0~255)
        return True
    else:
        return False



if __name__ == "__main__":
    main()
