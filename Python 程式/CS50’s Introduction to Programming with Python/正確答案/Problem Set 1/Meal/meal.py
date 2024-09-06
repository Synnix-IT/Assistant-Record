# Implement a program that prompts the user for a time and outputs whether it’s breakfast
# time, lunch time, or dinner time.
# Breakfast: 08:00 - 09:00
# Lunch: 12:00 - 13:00
# Dinner: 18:00 - 19:00

from typing import Final

def convert(time : str) -> float:

    MINUTES_IN_HOUR : Final[int] = 60               # 每小時有多少分鐘，常數

    hour : float = float(time.split(":")[0])        # 擷取時
    minute : float = float(time.split(":")[1])      # 擷取分

    return hour + (minute / MINUTES_IN_HOUR)        # 轉換成小數

def main():
    time : str = input("What time is it? ")

    time_in_decimal : float = convert(time)

    if 7.0 <= time_in_decimal <= 8.0:
        print("breakfast time")
    elif 12.0 <= time_in_decimal <= 13.0:
        print("lunch time")
    elif 18.0 <= time_in_decimal <= 19.0:
        print("dinner time")


if __name__ == "__main__":
    main()
