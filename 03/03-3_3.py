import os, re

f = open("friends101.txt", "r")

sentences = f.readlines()
f.close()
# print(sentences[:3])

# for i in sentences[:20]:
#     if re.match(r"[A-Z][a-z]+:", i):
#         print(i)

would = [i for i in sentences if re.match(r"[A-Z][a-z]+:", i) and re.search("would", i)]
# print(would)

newf = open("would.txt", "w")
newf.writelines(would)
newf.close()

take = [i for i in sentences if re.match(r"[A-Z][a-z]+:", i) and re.search("take", i)]
# print(take)
# for i in take:
#     print(i)