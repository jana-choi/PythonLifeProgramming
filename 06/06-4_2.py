import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

article = "https://news.v.daum.net/v/20200910171417882"
soup = bs(ur.urlopen(article).read(), "html.parser")

f = open("article_1.txt", "w", encoding="UTF-8")
for i in soup.find_all("p"):
    f.write(i.text)
f.close()