import json
import pprint

FILE_IN = "data/reddit_20190116.json"

FILE_OUT_JSON = "data/reddit_abridged.json"

FILE_OUT_CSV = "data/reddit_abridged.csv"

my_file = open(FILE_IN, "r")

my_data = json.load(my_file)

my_csv_file = open(FILE_OUT_CSV, "w")

# headers

my_csv_file.write("type,url,votes\n")

# pprint.pprint(my_data)

my_links = {'top': [], 'controversial': []}

for article in my_data['top']:
    pprint.pprint(article)

    my_links['top'].append(article['permalink'])

    my_csv_file.write("top," + article['permalink'] + "," + str(article['total_votes']) + "\n")

for article in my_data['controversial']:
    pprint.pprint(article)

    my_links['controversial'].append(article['permalink'])

    my_csv_file.write("controversial," + article['permalink'] + "," + str(article['total_votes']) + "\n")

my_file.close()
my_csv_file.close()

pprint.pprint(my_links)

my_file = open(FILE_OUT_JSON, "w")

json.dump(my_links, my_file, indent = 4)

my_file.close()

