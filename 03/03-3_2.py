import os, re, codecs

f = codecs.open("friends101.txt", "r", encoding="utf-8")

script101 = f.read()

character = [x[:-1] for x in list(set(re.findall(re.compile(r"[A-Z][a-z]+:"), script101)))]
print(character)

print(re.findall(r"\([A-Za-z].+[a-z|\.]\)", script101)[:6])