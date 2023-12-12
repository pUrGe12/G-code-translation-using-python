import requests
from bs4 import BeautifulSoup

webpage = requests.get('https://www.machinistguides.com/g-codes/').text
soup = BeautifulSoup(webpage, 'lxml')

valid_gcodes = []
for i in range(1,81):
    possible_gcode = soup.find_all('a', class_ = f'ez-toc-link ez-toc-heading-{i}')[0].text.strip().split(' ')[0][0:3]
    if possible_gcode.startswith('G'):
        valid_gcodes.append(possible_gcode)

print(valid_gcodes) 