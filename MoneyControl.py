import requests
from bs4 import BeautifulSoup


url = "https://www.moneycontrol.com/"
response = requests.get(url)
# print(response)
soup = BeautifulSoup(response.text, 'html.parser')

box_element = soup.find('div', class_='MR5 clearfix')

# Find all rows (tr elements) within the table
columns = box_element.find_all('td')

count = 0
data_list = []

for each in range(15):
    index_name = columns[count].find('a').text
    index_value = columns[count + 1].find('b').text
    change_value = columns[count + 2].text.strip()
    change_percent = columns[count + 3].text.strip()
    count += 4

    data = {
        "Index": index_name,
        "Value": index_value,
        "Change": change_value,
        "Percent Change": change_percent
    }

    data_list.append(data)

for dict_rec in data_list:
    print(dict_rec)
