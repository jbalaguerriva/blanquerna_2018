from collections import OrderedDict
import pprint
import re

def get_count(word):
    return word_counts[word]


FILE_NAME = "data/alice_in_wonderland.txt"

FILE_OUT = "data/alice_counts.csv"

my_file = open(FILE_NAME, "r")

my_lines = []

for line in my_file:
    my_lines.append(line.rstrip())

my_file.close()

word_counts = {}

for line in my_lines:
    words = re.split('\W+', line)
    #words = line.split(" ")
    # pprint.pprint(words)
    for word in words:
        if len(word) > 2:
            word_lower = word.lower()
            if word_lower not in word_counts:
                word_counts[word_lower] = 0
            word_counts[word_lower] = word_counts[word_lower] + 1

#pprint.pprint(word_counts)

words_ordered = sorted(word_counts.keys(), key = get_count, reverse = True)

file_out = open(FILE_OUT, "w")
file_out.write("word,count\n")

for word in words_ordered:
    print(word + "-->", word_counts[word])
    file_out.write(word + "," + str(word_counts[word]) + "\n")


file_out.close()







