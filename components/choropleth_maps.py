from urllib.request import urlopen
import json

with urlopen(
    "https://raw.githubusercontent.com/apisit/thailand.json/master/thailandWithName.json"
) as response:
    counties = json.load(response)

counties["features"][0]
