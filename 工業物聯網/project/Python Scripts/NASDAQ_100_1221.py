# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:32:11 2021

@author: 4080E008
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv('NASDAQ_100_Data_From_2010.csv', sep='\t')
#print(df.head(50))

df_AAPL = df[df['Name'].str.contains('AAPL')]
#print(df_AAPL.tail(50))#後50筆資料
mask = (df_AAPL['Date'] >= '2010-07-01') & (df_AAPL['Date'] < '2021-07-01')
df_AAPL = df_AAPL.loc[mask]
print('df_APPL套用時間的篩選條件回傳比數=',len(df_AAPL))
print(df_AAPL.tail(50))


df_TSLA = df[df['Name'].str.contains('TSLA')]
mask2 = (df_TSLA['Date'] >= '2010-07-01') & (df_TSLA['Date'] < '2021-07-01')
df_TSLA = df_TSLA.loc[mask2]
print('df_TSLA套用時間的篩選條件回傳比數=',len(df_TSLA))
print(df_TSLA.tail(50))
x_df = df_AAPL[['Close']]
y_df = df_TSLA[['Close']]

plt.xlabel('AAPL Price')
plt.ylabel('TSLA Price')

plt.scatter(df_AAPL.Close, df_TSLA.Close , color='red' , marker='*')

reg_model = linear_model.LinearRegression()
reg_model.fit(x_df, y_df)

print(reg_model.score(x_df,y_df))

m, b = np.polyfit(df_AAPL['Close'] ,df_TSLA['Close'], 1) #m = slope, b=intercept
print('slope m=', m)
print('intercept b=', b)
plt.plot(df_AAPL['Close'], m*df_AAPL['Close'] + b)

#print("AAPL=90 TSLA=",reg_model.predict([[90]]))
#print("AAPL=90 TSLA=",reg_model.predict([[120]]))
#print("AAPL=90 TSLA=",reg_model.predict([[150]]))