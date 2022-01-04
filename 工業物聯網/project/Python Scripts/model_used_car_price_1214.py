# -*- coding: utf-8 -*-
"""
Created on Tue Nov 30 11:32:11 2021

@author: 4080E008
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df = pd.read_csv('Used_Car_Price_Data.csv')
#print(df.head(5))


df = df[df['Name'].str.contains('Toyota Camry SE')]
#print(df.head(10))
df = df[df['Name'].str.contains('2019')]
#print(df.head(10))

plt.xlabel('Milage')
plt.xlabel('Price')

x_df = df[['Milage']]
y_df = df[['Price']]

select_texts = ['2019','2020']
str = '|'.join(select_texts)
df = df[df['Name'].str.contains(str)]
print('2019 or 2020結果:',len(df))

df['Milage'] = df['Milage'].str.replace(',','')
df['Price'] = df['Price'].str.replace(',','')
print(df.head(10))

df['Milage'] = df['Milage'].astype(float)
df['Price'] = df['Price'].astype(float)

plt.scatter(df.Milage , df.Price , color = 'red' , marker = '*')


reg_model = linear_model.LinearRegression()
#reg_model.fit(x_df, y_df)

#print(reg_model.score(x_df,y_df))

m,b = np.polyfit(df['Milage'],df['Price'],1)
print('slope m=',m)
print('intercept b=',b)
plt.plot(df['Milage'], m*df['Milage'] + b)

print("#Price for Milage=45000",reg_model.predict([[45000]]))
print("#Price for Milage=35000",reg_model.predict([[35000]]))
print("#Price for Milage=25000",reg_model.predict([[25000]]))



"""
#x_df = df.drop('cells',axis='columns')
x_df = df[['time']]
print(x_df)
print(x_df.dtypes)

y_df = df.cells
print(y_df)
print(y_df.dtypes)


print(reg_model.score(x_df,y_df))


#print("Predicted # cells ...", reg_model.predict([[2.3]]))

c = reg_model.intercept_
m = reg_model.coef_
print("from mannual calculation, cells =",(m*2.3)+c)

"""
