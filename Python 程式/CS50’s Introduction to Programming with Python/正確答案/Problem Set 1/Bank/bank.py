# If the greeting starts with “hello”, output $0.
# If the greeting starts with an “h” (but not “hello”), output $20.
# Otherwise, output $100. Ignore any leading whitespace in the user’s greeting,
# and treat the user’s greeting case-insensitively.

# Requirement
def bank() -> None:
    line : str = input("Greeting: ").strip().lower()        # 刪掉左右空格，轉換成小寫

    if line.startswith("hello"):                            # 使用 .startwith() 確認開頭
        print("$0")
    elif line.startswith("h"):
        print("$20")
    else:
        print("$100")


# Driver Code
if __name__ == "__main__":
    bank()
