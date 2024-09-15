# Implement a program that:

# Prompts the user for a level, n. If the user does not input 1, 2, or 3, the
# program should prompt again.

# Randomly generates ten (10) math problems formatted as X + Y = , wherein each
# of X and Y is a non-negative integer with n digits. No need to support
# operations other than addition (+).

# Prompts the user to solve each of those problems. If an answer is not correct
# (or not even a number), the program should output EEE and prompt the user
# again, allowing the user up to three tries in total for that problem. If the
# user has still not answered correctly after three tries, the program should
# output the correct answer.

# The program should ultimately output the user’s score: the number of correct
# answers out of 10.

from random import randint


def get_level() -> int:
    while True:
        level : str = input("")

        if level.isdigit() and 1 <= int(level) <= 3:
            break

    return int(level)


def generate_integer(level : int) -> list[str]:

    questions : list[str] = list()

    if level == 1:
        questions = [f"{randint(0, 9)} + {randint(0, 9)}" for index in range(0, 10)]
    else:
        questions = [f"{randint(pow(10, (level - 1)), pow(10, level))} + {randint(pow(10, (level - 1)), pow(10, level))}" for index in range(0, 10)]


    return questions


def main() -> None:
    level : int = get_level()

    questions : list[str] = generate_integer(level)

    score : int = 0

    for question in questions:
        for times in range(0, 3):
            print(f"{question} = ", end = "")
            answer : int = int(input())

            if answer == eval(question):
                score += 1
                break
            else:
                print(eval(question))
                print("EEE")

    print(f"Score: {score}")


if __name__ == "__main__":
    main()
