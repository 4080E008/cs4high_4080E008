# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:32:11 2021

@author: 4080E008
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv('cells.csv')
print(df.head(5))


plt.xlabel('time')
plt.xlabel('cells')
plt.scatter(df.time , df.cells , color = 'red' , marker = '*')


#x_df = df.drop('cells',axis='columns')
x_df = df[['time']]
print(x_df)
print(x_df.dtypes)

y_df = df.cells
print(y_df)
print(y_df.dtypes)

"""
reg_model = linear_model.LinearRegression()
reg_model.fit(x_df, y_df)


print(reg_model.score(x_df,y_df))
print("Predicted # cells ...", reg_model.predict([[5.0]]))

#print("Predicted # cells ...", reg_model.predict([[2.3]]))

c = reg_model.intercept_
m = reg_model.coef_
print("from mannual calculation, cells =",(m*2.3)+c)
"""
