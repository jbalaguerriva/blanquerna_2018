import csv
import pprint

FILE_IN = "data/reddit_abridged.csv"

my_file = open(FILE_IN, "r")

reader = csv.DictReader(my_file)

for row in reader:
    pprint.pprint(row)