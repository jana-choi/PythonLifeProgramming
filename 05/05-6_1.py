from scipy import stats
import pandas as pd

df2 = pd.read_csv("survey.csv")

male = df2.income[df2.sex == "m"]
female = df2.income[df2.sex == "f"]

ttest_result = stats.ttest_ind(male, female)
print(ttest_result)
print(ttest_result[0])
print(ttest_result[1])

if ttest_result[1] > .05:
    print("p-value는 {}로 95% 수준에서 유의하지 않음".format(ttest_result[1]))
else:
    print("p-value는 {}}로 95% 수준에서 유의함".format(ttest_result[1]))

corr = df2.corr()
print(corr)
print(df2.corr(method="spearman"))

print(df2.income.corr(df2.stress))

corr.to_csv("corr.csv")