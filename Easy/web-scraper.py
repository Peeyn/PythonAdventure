import requests
from bs4 import BeautifulSoup
import re

URL = "https://www.tvp.info/"

# make an HTTP request to the website
response = requests.get(URL)

# parse the HTML content of the page
soup = BeautifulSoup(response.text, "html.parser")

# find all the elements with class "story-heading"
headlines = soup.find_all(class_="news__title")
headlines += soup.find_all(class_="news__text")

#print the text of each headline
for headline in headlines:
    print(headline.text.strip())