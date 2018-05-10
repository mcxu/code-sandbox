"""
KNN is bad at handling outliers.

pandas drop documentation:
https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.drop.html
"""

import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd

pd.set_option('display.max_columns', 20)
pd.set_option('display.width', 1000)

df = pd.read_csv("data/breast_cancer/breast-cancer-wisconsin.data.txt")
df.replace('?', -99999, inplace=True) # this is recognized by sklearn as an outlier
df.drop(['id'], 1, inplace=True)
print(df.head(10))

x = np.array(df.drop(['class'], 1))
y = np.array(df['class'])