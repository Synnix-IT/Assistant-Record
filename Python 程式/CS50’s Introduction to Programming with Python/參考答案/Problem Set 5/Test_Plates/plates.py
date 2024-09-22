# Implement a program that prompts the user for a vanity plate and
# then output Valid if meets all of the requirements or Invalid if
# it does not. Assume that any letters in the user’s input will be uppercase.

from string import punctuation

def is_valid(plate : str) -> bool:

    if not plate[ : 2].isalpha() or not 2 <= len(plate) <= 6:           # 如果開頭兩個字不是字母，或長度不是 2 ~ 6
        return False

    if any(character in punctuation for character in plate):            # 如果有任何標點符號
        return False

    number_started = False                                              # 判斷是否已經是數字的 flag

    for character in plate:
        if not number_started and character == "0":                     # 如果數字開頭是 0
            return False

        if not number_started and character.isdigit():                  # 如果是數字，把 flag 變成 True
            number_started = True
            continue

        if number_started and character.isalpha():                      # 如果數字後面還有英文
            return False

    return True


def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
