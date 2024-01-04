# Use the BeautifulSoup and requests Python packages to print out 
# a list of all the article titles on the New York Times homepage.

import requests
from bs4 import BeautifulSoup

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

res = requests.get("https://www.nytimes.com/", verify=False)

soup = BeautifulSoup(res.text, "html.parser")
articles = soup.find_all("p", class_="indicate-hover css-66vf3i")

for value in articles:
    print(value.text)


