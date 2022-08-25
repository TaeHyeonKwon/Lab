import pandas as pd
import matplotlib.pyplot as plt
from xgboost import XGBRegressor
from pandas import concat
from pandas import *


days_in = 8
day_out = 1



df = pd.read_csv('timeSeries.csv')



df = df.drop(9,axis=0)
df = df.drop(10,axis=0)

df = df.loc[::-1]

valuse1 = df['exposure'].values



#df = df.drop(['Date'],axis=1)

df = DataFrame(valuse1)




raw = []

for i in range(days_in, 0 ,-1):
    raw.append(df.shift(i))
for i in range(0,day_out):
    raw.append(df.shift(-i))


sum = concat(raw,axis=1)


sum.dropna(inplace=True)

train = sum.values

trainX, trainy = train[:,:-1], train[:,-1]

model = XGBRegressor(objective='reg:squarederror',n_estimators=80)
model.fit(trainX,trainy)

data_in = valuse1[-(days_in):]
result = model.predict([data_in])


print('input: %s, Predicted: %.3f' %(data_in, result[0]))





