# Implement a function called convert that expects a str in any of the 12-hour
# formats below and returns the corresponding str in 24-hour format (i.e., 9:00
# to 17:00). Expect that AM and PM will be capitalized (with no periods therein)
# and that there will be a space before each.

# Assume that these times are representative of actual times, not necessarily
# 9:00 AM and 5:00 PM specifically.

# Raise a ValueError instead if the input to convert is not in either of those
# formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM, etc.). But do
# not assume that someone’s hours will start ante meridiem and end post
# meridiem; someone might work late and even long hours (e.g., 5:00 PM to 9:00
# AM).


import re
import sys


def getTime(time: str) -> list:
    TIME_FORMAT : str = r"^(\d{1,2})(?:\:)?(\d{2})? (AM|PM) to (\d{1,2})(?:\:)?(\d{2})? (AM|PM)$"

    matched_time : str = re.match(TIME_FORMAT, time, re.IGNORECASE)

    if matched_time:
        start_hour    : int = int(matched_time.group(1))
        start_minute  : int = int(matched_time.group(2)) if matched_time.group(2) else 0
        start_period  : str = (matched_time.group(3)).upper()

        end_hour      : int = int(matched_time.group(4))
        end_minute    : int = int(matched_time.group(5)) if matched_time.group(5) else 0
        end_period    : str = (matched_time.group(6)).upper()

        return [start_hour, start_minute, start_period, end_hour, end_minute, end_period]

    else:
        raise ValueError


def checkTime(time : list) -> None:
    start_hour, start_minute, _, end_hour, end_minute, _ = time

    if not 0 <= start_hour <= 12 or not 0 <= end_hour <= 12:
        raise ValueError

    if not 0 <= start_minute <= 59 or not 0 <= end_minute <= 59:
        raise ValueError


def convert(time : str) -> str:
    def convertTo24HourClock(hour : int, period : str) -> int:
        if period.upper() == "AM":
            return hour % 12
        elif period.upper() == "PM":
            return hour % 12 + 12

    start_hour, start_minute, start_period, end_hour, end_minute, end_period = time

    start_hour  = convertTo24HourClock(start_hour, start_period)
    end_hour    = convertTo24HourClock(end_hour, end_period)

    return f"{str(start_hour).zfill(2)}:{str(start_minute).zfill(2)} to {str(end_hour).zfill(2)}:{str(end_minute).zfill(2)}"


def main() -> None:
    time : str = input("Hours: ")

    try:
        formatted_time : list = getTime(time)
        checkTime(formatted_time)

    except ValueError:
        sys.exit("ValueError")

    print(convert(formatted_time))


if __name__ == "__main__":
    main()