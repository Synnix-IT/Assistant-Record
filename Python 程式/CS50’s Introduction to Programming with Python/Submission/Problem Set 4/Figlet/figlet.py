import pyfiglet
import sys


if (not sys.argv[1] == "-f" and not sys.argv[1] == "--font") or len(sys.argv) < 3:

    sys.exit("Invalid usage")

if not sys.argv[2] in pyfiglet.Figlet().getFonts():

    sys.exit("Invalid usage")

input_word : str =input("Input: ")

fig = pyfiglet.Figlet(font = sys.argv[2])

print(f"Output: \n{fig.renderText(input_word)}")
