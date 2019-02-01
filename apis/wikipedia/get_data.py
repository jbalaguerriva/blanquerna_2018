#https://pypi.org/project/wikipedia/

import json
import pprint
import wikipedia

wikipedia.set_lang("es")

result = wikipedia.search("Iglesias")

pprint.pprint(result)

page = wikipedia.page("Pablo Iglesias Turrión")

pprint.pprint(page.content)
pprint.pprint(page.url)
pprint.pprint(page.links)
pprint.pprint(page.summary)
pprint.pprint(page.html())
pprint.pprint(page.references)
pprint.pprint(page.images)

# pages = wikipedia.geosearch(41.398598,2.1654683, radius=10000)
#
# pprint.pprint(pages)
