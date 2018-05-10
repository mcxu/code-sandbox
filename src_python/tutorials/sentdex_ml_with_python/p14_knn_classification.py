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
df.drop(['id'], 1, inplace=True) # including id decreases accuracy
print(df.head(10))

x = np.array(df.drop(['class'], 1))
y = np.array(df['class'])

X = np.array(df.drop(['class'], 1))
y = np.array(df['class'])

X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2)

clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print("accuracy: ", accuracy)

example_measures = np.array([[4,2,1,1,1,2,3,2,1],
                             [4,2,1,2,2,2,3,2,1]]) # exluding id and class
example_measures = example_measures.reshape(2,-1) 
prediction = clf.predict(example_measures)
print("prediction: ", prediction)




