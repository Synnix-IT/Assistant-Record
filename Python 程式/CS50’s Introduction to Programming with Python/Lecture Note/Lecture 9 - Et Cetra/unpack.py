def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts


def main():
    coins = {"galleons": 100, "sickles": 50, "knuts": 25}

    print(f"{total(**coins)} Knuts")                        #使用 * 進行 list 解包，** 進行 dict 解包


if __name__ == "__main__":
    main()