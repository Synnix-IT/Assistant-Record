# Implement a program that prompts the user for the name of a file and
# then outputs that file’s media type if the file’s name ends, case-insensitively,
# in any of these suffixes:
# .gif
# .jpg
# .jpeg
# .png
# .pdf
# .txt
# .zip

def checkExtensions() -> None:
    file : str = input("File name: ").strip().lower()       # 刪掉左右空格，轉換成小寫

    extension_type = file[file.rfind(".") + 1 : ]           # 使用 .rfind() 來找到最後一個 "." 位置。擷取從該位置到結尾即為 Extension Type

    match extension_type:                                   # 標準 match-case
        case "gif":
            print("image/gif")
        case "jpg" | "jpeg":
            print("image/jpeg")
        case "png":
            print("image/png")
        case "pdf":
            print("application/pdf")
        case "txt":
            print("text/plain")
        case "zip":
            print("application/zip")
        case _:                                             # Wildcard case
            print("application/octet-stream")

if __name__ == "__main__":
    checkExtensions()
