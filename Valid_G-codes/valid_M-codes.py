import requests
from bs4 import BeautifulSoup

webpage = requests.get('https://linuxcnc.org/docs/html/gcode/m-code.html').text
soup = BeautifulSoup(webpage, 'lxml')

valid_mcodes = []
for i in range(0, 45, 2):
    for i in soup.find_all('p', class_ = 'table')[i].text.split(' '):
        valid_mcodes.append(i)
print(valid_mcodes)