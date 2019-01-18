# https://docs.python.org/3/library/pprint.html
# https://docs.python.org/3/library/csv.html

import csv
import pprint

FILE_IN = "data/reddit_abridged.csv"

my_file = open(FILE_IN, "r")

reader = csv.DictReader(my_file)

for row in reader:
    pprint.pprint(row)