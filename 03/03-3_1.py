import os, re, codecs

f = codecs.open("friends101.txt", "r", encoding="utf-8")

script101 = f.read()
# print(script101[:100])

Line = re.findall(r"Monica:.+", script101)
# print(Line[:3])
# for item in Line[:3]:
#     print(item)

f.close()

f = open("monica.txt", "w", encoding="utf-8")

monica = ""
for i in Line:
    monica += i.replace("\r", "") + "\n"
f.write(monica)

f.close()