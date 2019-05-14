import requests 
from bs4 import BeautifulSoup

resp = requests.get('http://www.naver.com/')
soup = BeautifulSoup(resp.text, 'html.parser')
hotkeywords = soup.select('ah_list . ah_item')

for hotkey in hotkeywords:
    print(f'{hotkey.select_one(".ah_r").get_text()}위'  
          f'{hotkey.select_one(".ah_k").get_text()}'
          f'{hotkey.select_one(".ah_a").get("href")}') 
          