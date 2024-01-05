"""
Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: 
http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.

The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can 
read the full article without having to click any buttons.
"""

import requests
from bs4 import BeautifulSoup


res = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
content = res.text

soup = BeautifulSoup(content, "html.parser")


title = soup.find(class_= "BaseWrap-sc-gjQpdd BaseText-ewhhUZ ContentHeaderHed-NCyCC iUEiRd euHXZX gydgrM")

print(title.text)

data = soup.find_all("p", class_="paywall")


for x in data:
    print(f"{x.text}\n\n")

