import json
import requests

dt=requests.get(r'https://raw.githubusercontent.com/johan/world.geo.json/master/countries/AFG.geo.json')
cont=json.loads(dt.text)
print(cont['features'][0]['geometry']['type'])

