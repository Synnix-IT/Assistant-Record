import re
import sys

def check24Hour(hour : int, period : str) -> int:                                                                                               #判斷上午下午並換算為24小時
    if period == "am":
        return int(hour % 12)
    elif period == "pm":
        return int(hour % 12 + 12)



def convert(times : str) -> str:

    if matches := re.match(r"(\d{1,2})(?::)?(\d{2})? (AM|PM) to (\d{1,2})(?::)?(\d{2})? (AM|PM)", times, re.IGNORECASE):                        #使用正則表達式驗證

        first_time_hour : int = int(matches.group(1))                                                                                           #設定正則表達式的分割結果
        first_time_minute : int = int(matches.group(2)) if matches.group(2) else int(0)
        first_time_period : str = matches.group(3).lower()
        second_time_hour : int = int(matches.group(4))
        second_time_minute : int = int(matches.group(5)) if matches.group(5) else int(0)
        second_time_period : str = matches.group(6).lower()

        if not (0 <= first_time_minute < 60 and 0 <= second_time_minute < 60 and 0 < first_time_hour <= 12 and 0 < second_time_hour <= 12):     #驗證輸入是否小時是否超過 12 小時;或是分鐘超過 60 分鐘
            sys.exit("ValueError")

        first_time_hour : int = check24Hour(first_time_hour, first_time_period)                                                                 #將上下午換算為 24 小時
        second_time_hour : int = check24Hour(second_time_hour, second_time_period)

        return (f"{first_time_hour:0>2d}:{first_time_minute:0>2d} to {second_time_hour:0>2d}:{second_time_minute:0>2d}")                        #回傳運算完的結果


    else:
        sys.exit("ValueError")

def main():
    print(convert(input("Hours: ").strip()))                                                                                                    #請使用者輸入並打印結果


if __name__ == "__main__":
    main()
