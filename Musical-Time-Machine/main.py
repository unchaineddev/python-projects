import requests
from bs4 import BeautifulSoup 

which_year = input("Enter the date you would like to travel back to in this format: YYYY-MM-DD: ")

URL = f"https://www.billboard.com/charts/hot-100/{which_year}"

response = requests.get(URL)

print(response)

soup = BeautifulSoup(response.text, 'html.parser')


hot100 = [title.getText(strip=True) for title in soup.select("li #title-of-a-story")]

print(hot100)

