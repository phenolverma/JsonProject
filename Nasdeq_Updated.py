import json
import requests

dt = requests.get(r'https://data.nasdaq.com/api/v3/datasets/XNSE/BAJAJ_AUTO.json?api_key=Mk7JfRK9zYexnn2VF__r')
cont = json.loads(dt.text)

sublist_len = len(cont['dataset']['data'])  # Checking length of the file

total_price = 0
day_count = 0
year = 2010
data_list = []

for year in range(2010, 2019):
    for each in range(sublist_len):
        if str(year) in cont['dataset']['data'][each][0]:
            total_price = cont['dataset']['data'][each][4] + total_price
            day_count += 1
    avg_total_price = total_price/365

    data_dict = {
        'Year': year,
        'Total Working Days': day_count,
        'Avg Closing Price': avg_total_price
    }

    data_list.append(data_dict)
    total_price = 0
    day_count = 0

for each in data_list:
    print(each)

