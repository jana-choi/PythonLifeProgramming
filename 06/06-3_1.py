import os, re
import urllib.request as ur
from bs4 import BeautifulSoup as bs

news = "https://news.daum.net/"
soup = bs(ur.urlopen(news).read(), "html.parser")
# print(soup)

# issue = soup.find_all("div", {"class":"item_issue"})
# print(issue)
# for i in issue:
#     print(i.text)

# hyperlink = soup.find_all("a")
# print(hyperlink[:5])
# for h in hyperlink:
#     print(h.get("href"))

# for i in issue:
#     print(i.find_all("a")[0].get("href"))

headline = soup.find_all("div", {"class":"item_issue"})
for i in headline:
    print("\n\n========================================================================\n")
    print(i.text)
    soup2 = bs(ur.urlopen(i.find_all("a")[0].get("href")).read(), "html.parser")
    for j in soup2.find_all("p"):
        print(j.text)