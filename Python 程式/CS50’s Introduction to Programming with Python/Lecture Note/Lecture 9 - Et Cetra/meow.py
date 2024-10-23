import argparse


parser = argparse.ArgumentParser(description = "Meow like a cat.")                      #代替 sys.argv
parser.add_argument("-n", default = 1, help = "Number of times to meow", type = int)    #代替 sys.argv， -n 代表輸入空白後的數，default 代表預設值，help 表示說明，type 代表輸入型態
args = parser.parse_args()

print("meow\n" * args.n , end="")