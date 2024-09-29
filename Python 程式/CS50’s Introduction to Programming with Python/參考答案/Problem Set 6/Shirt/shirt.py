# Implement a program that expects exactly two command-line arguments:

#   in sys.argv[1], the name (or path) of a JPEG or PNG to read (i.e., open) as input
#   in sys.argv[2], the name (or path) of a JPEG or PNG to write (i.e., save) as output

# The program should then overlay shirt.png (which has a transparent background) on the input after
# resizing and cropping the input to be the same size, saving the result as its output.

# The program should instead exit via sys.exit:

#   if the user does not specify exactly two command-line arguments,
#   if the input’s and output’s names do not end in .jpg, .jpeg, or .png, case-insensitively,
#   if the input’s name does not have the same extension as the output’s name, or
#   if the specified input does not exist.


import os
from PIL import Image, ImageFile, ImageOps
import sys
from typing import List, Final, Tuple


SUPPOSED_ARGUMENT_COUNT : Final[int] = 3

ACCEPTED_EXTENSION : Final[Tuple[str, ...]] = (".jpg", ".jpeg", ".png")


def checkArguments(argument : List[str]) -> Tuple[str, str]:
    if len(argument) < SUPPOSED_ARGUMENT_COUNT:
        sys.exit("Too few command-line arguments")

    if len(argument) > SUPPOSED_ARGUMENT_COUNT:
        sys.exit("Too many command-line arguments")

    input_file = argument[1]
    output_file = argument[2]

    input_extension : str = os.path.splitext(input_file)[1].lower()
    output_extension : str = os.path.splitext(output_file)[1].lower()

    if (input_extension == "" or output_file == "") or (input_extension not in ACCEPTED_EXTENSION or output_extension not in ACCEPTED_EXTENSION):
        sys.exit("Invalid arguments")

    if input_extension != output_extension:
        sys.exit("Input and output have different extensions")

    return input_file, output_file


def processPhoto(input_file : str, output_file : str) -> None:
    try:
        input_image : ImageFile.ImageFile = Image.open(input_file, "r")

    except FileNotFoundError:
        sys.exit("File does not exist")

    shirt : ImageFile.ImageFile = Image.open("shirt.png", "r")
    size : Tuple[int, int] = shirt.size
    fitted_image : Image.Image = ImageOps.fit(input_image, size)
    fitted_image.paste(shirt, (0, 0), shirt)
    fitted_image.save(output_file)


def main() -> None:
    input_file : str = None
    output_file : str = None
    input_file, output_file = checkArguments(sys.argv)

    processPhoto(input_file, output_file)


if __name__ == "__main__":
    main()