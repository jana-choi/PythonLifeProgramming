import os, re

f = open("friends101.txt", "r")

sentences = f.readlines()
# print(sentences[:3])

for i in sentences[:20]:
    if re.match(r"[A-Z][a-z]+:", i):
        print(i)