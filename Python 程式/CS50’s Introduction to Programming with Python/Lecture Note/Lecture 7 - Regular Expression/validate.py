import re

email = input("What's your email? ").strip()

#user_name, user_domain = email.split("@")

#if user_name and "." in user_domain:
#if user_name and user_domain.endswith(".edu"):
#    print("Valid")
#else:
#    print("Invalid")

#if re.search(r"^.+@.+\.edu$", email):                                                   #使用正則表達式驗證; ^ 代表開頭; $ 代表結尾; + 代表一個或多個; . 代表任意字元; \ 代表特殊字元; 
#if re.search(r"^[^@]+@[^@]+\.edu$", email):                                             #[^@] 代表不包含 @ 的任何字元
#if re.search(r"^[a-zA-Z0-9_]+@[a-zA-Z0-9_]+\.edu$", email):                             #[a-zA-Z0-9_] 代表包含 a~z, A~Z, 0~9, _ 的任何字元  
#if re.search(r"^\w+@\w+\.(edu|com|gov|net|org)$", email, re.IGNORECASE):                #\w 代表包含 a~z, A~Z, 0~9, _ 的任何字元, | 代表或; re.IGNORECASE 代表忽略大小寫
#if re.search(r"^\w+@(\w+\.)?\w+\.(edu|com|gov|net|org)$", email, re.IGNORECASE):        #? 代表前一個條件可以 0 或 1 次
if re.fullmatch(r"\w+@(\w+\.)?\w+\.(edu|com|gov|net|org)", email, re.IGNORECASE):        #使用 fullmatch 可以驗證完整的email，並省略開頭的 ^ 結尾的 $
    print("Valid")
else:
    print("Invalid")
