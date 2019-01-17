# https://www.gutenberg.org/browse/scores/top

FILE_NAME = "data/alice_in_wonderland.txt"

my_file = open(FILE_NAME, "r")

for line in my_file:
    line = line.rstrip()
    print(line)

my_file.close()


