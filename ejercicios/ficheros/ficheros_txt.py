# https://www.gutenberg.org
# https://docs.python.org/3/library/stdtypes.html#string-methods
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

FILE_NAME = "data/alice_in_wonderland.txt"

my_file = open(FILE_NAME, "r")

for line in my_file:
    line = line.rstrip()
    print(line)

my_file.close()


