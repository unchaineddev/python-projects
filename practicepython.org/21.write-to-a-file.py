# Take the code from the How To Decode A Website exercise 
# (if you didn’t do it or just want to play with some different code, 
# use the code from the solution), and instead of printing the results 
# to a screen, write the results to a txt file. 
# In your code, just make up a name for the file you are saving to.
# Extras: Ask the user to specify the name of the output file that will be saved.


import requests
from bs4 import BeautifulSoup

import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

res = requests.get("https://www.nytimes.com/", verify=False)

soup = BeautifulSoup(res.text, "html.parser")
articles = soup.find_all("p", class_="indicate-hover css-66vf3i")


# writing to file 
file = input("To save it to a file, enter file name: ")
for value in articles:
    with open(f"{file}.txt", "a") as f:
        f.write(f'{value.text}\n')




