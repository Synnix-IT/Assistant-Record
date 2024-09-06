import string

delete = str.maketrans({"," : "", "!" : "", "." : ""})
text = input("Greeting: ").translate(delete).lower()

word = text.split()

if word[0] in "hello":
    print("$0")
elif text[0] == "h":
    print("$20")
else:
    print("$100")
