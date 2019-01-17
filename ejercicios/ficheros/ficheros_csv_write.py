import csv
import pprint

FILE_IN = "data/reddit_abridged.csv"
FILE_OUT = "data/reddit_top.csv"

my_file_in = open(FILE_IN, "r")

my_file_out = open(FILE_OUT, "w")


reader = csv.DictReader(my_file_in)

writer = csv.DictWriter(my_file_out, fieldnames = ['url', 'votes'])

writer.writeheader()

for row in reader:

    writer.writerow({'url': row['url'], 'votes': row['votes']})
    pprint.pprint(row)