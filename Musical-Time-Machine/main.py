
import os
import requests
from bs4 import BeautifulSoup 
import spotipy
from spotipy.oauth2 import SpotifyOAuth

from dotenv import load_dotenv
load_dotenv()


CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET= os.getenv("CLIENT_SECRET")





# Scraping BillBoard Hot 100 
which_year = input("Enter the date you would like to travel back to in this format: YYYY-MM-DD: ")
URL = f"https://www.billboard.com/charts/hot-100/{which_year}"
response = requests.get(URL)
#print(response)
soup = BeautifulSoup(response.text, 'html.parser')
hot100 = [title.getText(strip=True) for title in soup.select("li #title-of-a-story")]
print(hot100)


# Authentication

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        client_id=CLIENT_ID,
        client_secret=CLIENT_SECRET,
        scope="playlist-modify-private",
        redirect_uri="http://localhost:8888/callback",
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]

print(user_id)
