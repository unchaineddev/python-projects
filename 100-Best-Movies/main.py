import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)
website_url = response.text

# parse the url in html
soup = BeautifulSoup(website_url, "html.parser")
movie_list = soup.find_all(name="h3", class_ ="title")
#print(movie_list)

# List comprehension to get the titles
movie_title = [movie.getText() for movie in movie_list] 


# reverse a string 
#print(movie_title[::-1])

#### or use below to rev a string #### 

#for n in range(len(movie_title) -1, -1, -1):
 #   print(movie_title[n])


movies = movie_title[::-1]


with open("movies.txt", mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")
