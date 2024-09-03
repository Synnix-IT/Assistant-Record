from random import randint                                                                      # 產生隨機數。由於只需要用到 "randint"，所以只匯入這個函式
import general

def ultimate_code_game() -> None:                                                               # 將主程式變成一個函式有利於將程式結構化，也可以讓程式碼更容易閱讀
    """
    Play the ultimate code guessing game.

    1. Prompt the user to input the minimum, maximum, and the number of times to guess.
    2. Generate a random number within the range of minimum and maximum as the answer.
    3. Start the game, and the user will have the specified number of times to guess the answer.
    4. After each guess, give a hint, whether the guess is too small or too large.
    5. If the user guesses correctly, the game will end and the user will win.
    6. If the user has used up all the guesses, the game will end and the user will lose.
    """
    print("終極密碼規則設定")

    minimum, maximum, times = general.getInput()                                                # 取得使用者輸入的最小值、最大值、猜測次數，用 tuple 儲存會比一個一個慢慢宣告來得快

    answer = randint(minimum, maximum)                                                          # 隨機產生終極密碼

    print(f"終極密碼開始，範圍 {minimum} ~ {maximum}")                                              # f-string 可以讓字串中的變數直接被替換。格式為 f"...{變數}"

    for i in range(times):                                                                      # 猜測次數為 times，每次猜測後剩餘次數 - 1
        while True:
            guess = input("請輸入猜測數字: ")

            if general.checkInput(guess):                                                       # 檢查輸入是否為數字
                guess = int(guess)                                                              # 轉換為整數

                if minimum <= guess <= maximum:                                                 # 檢查猜測數字是否在範圍內
                    break
                else:
                    print(f"超過範圍，請輸入範圍 {minimum} ~ {maximum} 之間的數字")

            else:
                print("請輸入有效的數字")

        if guess == answer:
            print(f"恭喜答對，答案是: {answer}")
            return
        elif guess < answer:
            print(f"猜小了，剩餘次數: {times - i - 1}")
            minimum = guess + 1                                                                 # 猜測數字小於終極密碼，則最小值改為猜測數字 + 1
        else:
            print(f"猜大了，剩餘次數: {times - i - 1}")
            maximum = guess - 1                                                                 # 猜測數字大於終極密碼，則最大值改為猜測數字 - 1

        print(f"範圍 {minimum} ~ {maximum}")

    print(f"很遺憾，您已經用完所有猜測次數。正確答案是: {answer}")


if __name__ == "__main__":
    ultimate_code_game()