#https://www.tronalddump.io/

import requests
import json
import pprint


query_one = requests.get("https://api.tronalddump.io/search/quote", params= {'query': "obama"}).json()

query_two = requests.get("https://api.tronalddump.io/search/quote", params= {'query': "bernie sanders"}).json()

# pprint.pprint(query_two)

for quote in query_two["_embedded"]["quotes"]:
    print(quote['value'])
    print("=========")
