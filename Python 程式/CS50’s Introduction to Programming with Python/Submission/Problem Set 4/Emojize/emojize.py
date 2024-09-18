from emoji import emojize

print(f"Output: {emojize(input("Input: "), language = "alias")}")

#print(f"Output: {emojize(input("Input: "), use_aliases = True)}")  目測答案一樣，確認結果卻是錯誤
