# Calculate the tip based on total and tip percentage


def dollars_to_float(dollars : str) -> float:

    return float(dollars.replace("$", ""))


def percent_to_float(percent : str) -> float:

    return float(percent.replace("%", "")) / 100


# Main function
def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))

    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


if __name__ == "__main__":
    main()