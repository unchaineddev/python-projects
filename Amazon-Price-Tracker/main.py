import requests
import bs4
import lxml
from bs4 import BeautifulSoup
from smtplib import SMTP


BUY_PRICE = 3500

USER="###############"
EMAIL="##############"


URL = "https://www.amazon.in/Elements-Portable-External-Drive-Black/dp/B00PLOXG42/ref=sr_1_1_sspa?keywords=harddrive&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"


headers = {
    'Accept-Language': "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8",
    'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}


Response = requests.get(URL, headers=headers)
#print(Response.text)


soup = BeautifulSoup(Response.content, 'lxml')
#print(soup.prettify())


title = soup.find(id="productTitle").getText()
#print(title)


price = soup.find(name='span', class_="a-offscreen").getText()
#print(price)


split_price = price.split("₹")
s = split_price[1].replace(","," ").replace(" ", "")
final_price = float(s)
#print(final_price)


if final_price < BUY_PRICE:
    message = f"{title} is now {final_price}"

    with smtplib.SMTP(host="smtp-mail.outlook.com") as new_connect:
        new_connect.starttls()

        new_connect.login(user=USER, email=EMAIL)
        new_connect.sendmail(from_addr=USER, to_addrs="#######", msg="Subject {title} -- price \n\n Hi, {title} has reduced to {BUY_PRICE}" )
