# https://www.crummy.com/software/BeautifulSoup/bs4/doc/
from bs4 import BeautifulSoup
import requests
import pprint
import csv

URL = "https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate"

FILE_OUT = "homicides.csv"

page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')


pprint.pprint(soup.findAll("a"))

for node in soup.findAll("a"):
    pprint.pprint(node)
    pprint.pprint(node.attrs)
    pprint.pprint(node.get("href"))
    print("========================")



# With third wikitable

my_table = soup.select("table.wikitable")[2]

row_number = 0

header = []
data = []

for row in my_table.select("tr"):
    if row_number == 0:
        for col in row.select("th"):
            pprint.pprint(col.get_text().rstrip())
            header.append(col.get_text().rstrip())
    else:
        if row_number > 1:
            new_row = []

            for col in row.select("td"):
                pprint.pprint(col.get_text().lstrip().rstrip())
                new_row.append(col.get_text().lstrip().rstrip())

            data.append(new_row)
    row_number+=1


# Write header + data

my_file = open(FILE_OUT, "w")

csv_writer = csv.writer(my_file)

csv_writer.writerow(header)

for row in data:
    csv_writer.writerow(row)

my_file.close()

