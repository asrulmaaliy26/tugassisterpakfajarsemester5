import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
import json

driver = webdriver.Chrome()
driver.get('https://id.wikipedia.org/wiki/Daftar_kota_di_Indonesia_menurut_provinsi')
results = []

# Wait for the table to load (you may need to adjust the wait time)
import time
time.sleep(5)

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')

table = soup.find('table', {'class': 'wikitable'})
rows = table.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    cols = [col.text.strip() for col in cols]
    results.append(cols)

# Remove empty rows
results = [result for result in results if result]

# Convert the data to a JSON structure
data = []
for result in results:
    if len(result) == 4:
        data.append({
            'No': result[0],
            'Province': result[1],
            'City': result[2],
            'Region': result[3]
        })

# Save the data as JSON
filename = 'city_data.json'
with open(filename, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

driver.quit()
