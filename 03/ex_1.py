import re

words = ["apple", "cat", "brave", "drama", "arise", "blow", "coat", "above"]
for i in words:
    m = re.match(r"a\D+", i)
    if m:
        print(m.group())