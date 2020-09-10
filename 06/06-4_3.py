import os, re, datetime
import urllib.request as ur
from bs4 import BeautifulSoup as bs

news = "https://news.daum.net/"
soup = bs(ur.urlopen(news).read(), "html.parser")

f = open(str"article_total.txt", "w", encoding="UTF-8")

for i in soup.find_all("div", {"class":"item_issue"}):
    try:
        f.write(i.text + "\n")
        f.write(i.find_all("a")[0].get("href") + "\n")
        soup2 = bs(ur.urlopen(i.find_all("a")[0].get("href")).read(), "html.parser")
        for j in soup2.find_all("p"):
            f.write(j.text)
    except:
        pass

f.close()