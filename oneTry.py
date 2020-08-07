# python webscrape2 with BeautifulSoup

from bs4 import BeautifulSoup
import requests
from user_agent import generate_user_agent, generate_navigator
from pprint import pprint
import urllib3.request

from requests import get
url = 'uurlHere'
# response = get(url)

# page_response = requests.get(url, timeout=5)
http = urllib3.PoolManager()
with http.request('GET', url) as response:
    page_response = response.read().decode('utf-8')
html_soup = BeautifulSoup(page_response.text, 'html.parser')
type(html_soup)

card_title_containers = html_soup.find_all('div', class_ = 'profile-card-title')
# card_title_containers = html_soup.find_all('div')
print(type(card_title_containers))
print(len(card_title_containers))


document.querySelector("body > app-root > div > div > main > app-home > div > div > platform-page-container > div > div > div > div.home-location-network.ng-tns-c22-3.ng-star-inserted > span.home-location.middle-input")
