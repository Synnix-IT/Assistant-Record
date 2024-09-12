def get_int() -> int:
    while True:
        try :
            number : int = int(input("What's number? "))
            return number
        
        except ValueError:
            print("number isn't an integer")

def main():

    print(f"number is {get_int()}")    

main()