# https://www.gutenberg.org
# https://docs.python.org/3/library/stdtypes.html#string-methods
# https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files

FILE_NAME = "data/alice_in_wonderland.txt"

my_file = open(FILE_NAME, "r")

contador = 0

for line in my_file:
    line = line.rstrip()
    alice_in_line = line.count("Alice")
    contador = contador + alice_in_line

print("APAREZCO ", contador, " VECES")

my_file.close()


