import statsmodels.formula.api as smf
import pandas as pd

df2 = pd.read_csv("survey.csv")

model = smf.ols(formula = "jobSatisfaction~English", data = df2)
result = model.fit()
print(result.summary())

model2 = smf.ols(formula = "jobSatisfaction~English + stress + income", data = df2)
result = model2.fit()
print(result.summary())