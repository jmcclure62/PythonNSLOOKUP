# From https://hackersandslackers.com/scraping-urls-with-beautifulsoup/
# LOOK https://stackoverflow.com/questions/46987241/using-beautifulsoup-where-authentication-is-required

import requests
from bs4 import BeautifulSoup

# Set Headers

url = "https://google.com"
req = requests.get(url)
soup = BeautifulSoup(req.content, 'html.parser')
print(soup.prettify())