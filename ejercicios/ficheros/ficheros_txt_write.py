# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://docs.python.org/3/library/stdtypes.html#string-methods
# https://docs.python.org/3/library/pprint.html

import pprint

FILE_IN_NAME = "data/alice_in_wonderland.txt"
FILE_OUT_NAME = "data/alice_in_wonderland_i.txt"

# Read file into my_lines list

my_file = open(FILE_IN_NAME, "r")

my_lines = []

for line in my_file:
    my_lines.append(line.rstrip())

my_file.close()

# Write file line by line subbing i for vowels

my_file = open(FILE_OUT_NAME, "w")

for line in my_lines:

    line = line.replace("a", "i")
    line = line.replace("e", "i")
    line = line.replace("i", "i")
    line = line.replace("o", "i")
    line = line.replace("u", "i")

    line = line.replace("A", "I")
    line = line.replace("E", "I")
    line = line.replace("I", "I")
    line = line.replace("O", "I")
    line = line.replace("U", "I")

    print(line)

    my_file.write(line + "\n")

my_file.close()






