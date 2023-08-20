import requests
from bs4 import BeautifulSoup

url = "https://www.wrldc.in/"

# Send an HTTP GET request to the URL
response = requests.get(url)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Find the element that contains the frequency data
box_element = soup.find('div', class_='content')  # Adjust the class name as needed

date_time_element = box_element.find('strong', id='dataDateTime')
demand_element = box_element.find('strong', id='dataDemand')
frequency_element = box_element.find('strong', id='dataFrequency')
renewable_element = box_element.find('strong', id='dataRenewable')
revision_element = box_element.find('strong', id='dataRevision')

date_time_value = date_time_element.get_text(strip=True)
demand_value = demand_element.get_text(strip=True)
frequency_value = frequency_element.get_text(strip=True)
renewable_value = renewable_element.get_text(strip=True)
revision_value = revision_element.get_text(strip=True)

data = {
        "DATE TIME": date_time_value,
        "DEMAND": demand_value,
        "FREQUENCY": frequency_value,
        "RENEWABLE": renewable_value,
        "REVISION NOS": revision_value
    }

for each in data:
    print(f'- {each} -  {data[each]}')

