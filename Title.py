import re
import requests

sites = ['https://www.google.com/', 'https://www.flipkart.com', 'https://www.amazon.in/', 'https://www.wrldc.in/']
for s in sites:
    resp = requests.get(s)
    # print(resp)
    # print('Successfully opened')
    pat = '<title>.*</title>'
    matcher = re.finditer(pat, resp.text)
    for i in matcher:
        print('Title: ', i.group())
