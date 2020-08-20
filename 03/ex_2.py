import re

a = "제 이메일 주소는 greatking@nanver.com입니다. 오늘 저는 travel@daum.net 라는 주소로 메일을 보내려고 합니다. 저는 apple@gmail.com, life@abc.co.kr 라는 메일도 사용하고 있습니다."
b = re.findall(r"[a-z]+@[a-z]+[a-z.]+", a)
print(b)