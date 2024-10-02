# Implement a program that prompts the user for an email address via input and
# then prints Valid or Invalid, respectively, if the input is a syntactically
# valid email address.


import validators


def main() -> None:
    email : str = input("What's your email address? ")

    if (validators.email(email)):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()