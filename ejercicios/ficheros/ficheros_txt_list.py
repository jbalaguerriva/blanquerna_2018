# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
# https://docs.python.org/3/library/pprint.html
# https://docs.python.org/3/library/

import pprint

FILE_NAME = "data/alice_in_wonderland.txt"

my_file = open(FILE_NAME, "r")

my_lines = []

for line in my_file:
    my_lines.append(line.rstrip())

my_file.close()

#pprint.pprint(my_lines)

for line in my_lines:
    print(line)




