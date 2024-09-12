# Implement a program that prompts the user for the name of a variable in camel case and
# outputs the corresponding name in snake case. Assume that the user’s input will indeed
# be in camel case.

def snakeCase() -> None:
    name : str = input("camelCase: ")

    for character in name:
        if character.isupper():                                         # 如果該字母為大寫的話
            name = name.replace(character, f"_{character.lower()}")     # 將該字母替換成 _{該字母小寫}

    print(name)


if __name__ == "__main__":
    snakeCase()
