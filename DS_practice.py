import pandas as pd
import numpy as np

import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression

import statsmodels.api as sm

data = pd.read_csv("data/Advertising.csv", index_col=0)

## SIMPLE LINEAR REGRESSION

plt.figure(figsize=(16,8))
plt.scatter(data['TV'], data['sales'], c='black')
plt.xlabel('Money spent on TV ads ($)')
plt.ylabel('Sales ($1000)')