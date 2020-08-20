import re

exam = "저는 92년에 태어났습니다. 88년에는 올림픽이 있었습니다. 지금은 2020년입니다."
print(re.findall("\d.+?년", exam))