import re


def count(um):

    matches_um = re.findall(r"\bum\b", um, re.IGNORECASE)


    return len(matches_um)

def main():

    print(count(input("Text: ")), end = "")

if __name__ == "__main__":
    main()

