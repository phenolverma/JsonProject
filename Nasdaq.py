import json
import requests

dt = requests.get(r'https://data.nasdaq.com/api/v3/datasets/XNSE/BAJAJ_AUTO.json?api_key=Mk7JfRK9zYexnn2VF__r')
cont = json.loads(dt.text)

sublist_len = len(cont['dataset']['data'])  # Checking length of the file

total_price_2010 = 0
total_price_2011 = 0
total_price_2012 = 0
total_price_2013 = 0
total_price_2014 = 0
total_price_2015 = 0
total_price_2016 = 0
total_price_2017 = 0
total_price_2018 = 0

day_count_2010 = 0
day_count_2011 = 0
day_count_2012 = 0
day_count_2013 = 0
day_count_2014 = 0
day_count_2015 = 0
day_count_2016 = 0
day_count_2017 = 0
day_count_2018 = 0

for each in range(sublist_len):
    if '2010' in cont['dataset']['data'][each][0]:
        total_price_2010 = cont['dataset']['data'][each][4] + total_price_2010
        day_count_2010 += 1

    if '2011' in cont['dataset']['data'][each][0]:
        total_price_2011 = cont['dataset']['data'][each][4] + total_price_2011
        day_count_2011 += 1

    if '2012' in cont['dataset']['data'][each][0]:
        total_price_2012 = cont['dataset']['data'][each][4] + total_price_2012
        day_count_2012 += 1

    if '2013' in cont['dataset']['data'][each][0]:
        total_price_2013 = cont['dataset']['data'][each][4] + total_price_2013
        day_count_2013 += 1

    if '2014' in cont['dataset']['data'][each][0]:
        total_price_2014 = cont['dataset']['data'][each][4] + total_price_2014
        day_count_2014 += 1

    if '2015' in cont['dataset']['data'][each][0]:
        total_price_2015 = cont['dataset']['data'][each][4] + total_price_2015
        day_count_2015 += 1

    if '2016' in cont['dataset']['data'][each][0]:
        total_price_2016 = cont['dataset']['data'][each][4] + total_price_2016
        day_count_2016 += 1

    if '2017' in cont['dataset']['data'][each][0]:
        total_price_2017 = cont['dataset']['data'][each][4] + total_price_2017
        day_count_2017 += 1

    if '2018' in cont['dataset']['data'][each][0]:
        total_price_2018 = cont['dataset']['data'][each][4] + total_price_2018
        day_count_2018 += 1

print(f'Avg Closing Price for 2010 for {day_count_2010} days - {total_price_2010 / 365}')
print(f'Avg Closing Price for 2011 for {day_count_2011} days - {total_price_2011 / 365}')
print(f'Avg Closing Price for 2012 for {day_count_2012} days - {total_price_2012 / 365}')
print(f'Avg Closing Price for 2013 for {day_count_2013} days - {total_price_2013 / 365}')
print(f'Avg Closing Price for 2014 for {day_count_2014} days - {total_price_2014 / 365}')
print(f'Avg Closing Price for 2015 for {day_count_2015} days - {total_price_2015 / 365}')
print(f'Avg Closing Price for 2016 for {day_count_2016} days - {total_price_2016 / 365}')
print(f'Avg Closing Price for 2017 for {day_count_2017} days - {total_price_2017 / 365}')
print(f'Avg Closing Price for 2018 for {day_count_2018} days - {total_price_2018 / 365}')
