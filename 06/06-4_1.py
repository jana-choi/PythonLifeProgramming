import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

news = "https://news.daum.net/"
soup = bs(ur.urlopen(news).read(), "html.parser")

f = open("links.txt", "w")

for i in soup.find_all("div", {"class":"item_issue"}):
    f.write(i.find_all("a")[0].get("href") + "\n")

f.close()