
import requests
from bs4 import BeautifulSoup

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
cookie = '_zitok=50eb0870dd8a91c1a8411702360585'
header = {'User-Agent': user_agent, 'Cookie': cookie}

web = requests.get('https://machmotion.com/downloads/GCode/10267.txt', headers = header).text
soup = BeautifulSoup(web, 'lxml')

G_code_unlisted = soup.find('p').text
G_code_listed = soup.find('p').text.split()
