import os, re, usecsv
import requests
import urllib.request as ur
from bs4 import BeautifulSoup as bs

soup = bs(ur.urlopen("http://quotes.toscrape.com/").read(), "html.parser")
# print(soup)

# quote = soup.find_all("span")
# for i in quote:
#     print(i.text)

quote = soup.find_all("div", {"class":"quote"})
for i in quote:
    print(i.text)