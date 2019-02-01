#https://newsapi.org/

import json
import pprint
import requests

API_KEY = "2082a4f4323c4119a0250003bd826622"

# Spanish sources

results = requests.get("https://newsapi.org/v2/sources", params = {"country": "es","apiKey": API_KEY}).json()

pprint.pprint(results)

# Sources all around

results = requests.get("https://newsapi.org/v2/sources", params = {"apiKey": API_KEY}).json()

pprint.pprint(results)

# Top headlines from reddit

results = requests.get("https://newsapi.org/v2/top-headlines", params = {"sources": "reddit-r-all", "apiKey": API_KEY}).json()

pprint.pprint(results)


# All articles mentioning facebook in last month

results = requests.get("https://newsapi.org/v2/everything", params = {"q": "facebook", "language": "es", "from": "2019-01-31","apiKey": API_KEY, "pageSize": 100}).json()

pprint.pprint(results)

pprint.pprint(len(results['articles']))
