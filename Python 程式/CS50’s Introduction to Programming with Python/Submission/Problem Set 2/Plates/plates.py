def main():
    plate : str = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def checkWord(word : str , flag : bool) -> bool:

    if flag == True and word.isalpha():
        return False

    if flag == False and word.isdigit() and word == "0":
        return False

    if word.isdigit():
        return True


def is_valid(brand_number : str) -> bool:

    if (not brand_number[0:1].isalpha()) or (not 2 <= len(brand_number) <= 6) or (not brand_number.isalnum()):
        return False

    flag : bool = False

    for item in brand_number:
        if checkWord(item, flag) :
            flag = checkWord(item, flag)

        elif checkWord(item, flag) == False:
            return False

    return True

main()
