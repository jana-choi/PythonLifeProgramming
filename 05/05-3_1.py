import numpy as np

discount = .05  # 할인율 5%
cashflow = 100  # 현금 흐름 100(억 원)

def presentvalue(n):    # 자본의 현재 가치
    return (cashflow / ((1 + discount) ** n))

# print(presentvalue(1))  # 1년이 지났을 때 자본의 현재 가치
# print(presentvalue(2))  # 2년이 지났을 때 자본의 현재 가치

for i in range(20):
    print(presentvalue(i))