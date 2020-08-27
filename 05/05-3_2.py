import numpy as np
import numpy_financial as npf

loss = [-750, -250]     # 1, 2년 차에 발생한 비용
profit = [100] * 18     # 3년 차부터 발생한 이익
cf = loss + profit      # 총 20년 동안의 현금 흐름 리스트
# print(cf)

cashflow = np.array(cf)
print(cashflow)

npv = npf.npv(0.045, cashflow)   # 순현재가치
print(npv)

irr = npf.irr(cashflow)          # 내부수익률
print(irr)