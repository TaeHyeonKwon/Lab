import inline as inline
import pandas as pd
from datetime import datetime,timedelta
from xgboost import XGBRegressor
from pandas import concat
from pandas import *




df = pd.read_csv('C:/Users/USER/Desktop/instagram.csv',encoding='cp949')



df = df.drop(['Unnamed: 0', '활동영역','게시일'],axis='columns')


df = df.rename(columns={'노출':'exposure','도달':'reach','공감':'like','댓글':'comment'})



df = df.drop(9,axis=0)
df = df.drop(10,axis=0)



days_in = len(df['exposure'])-1
day_out = 1

exposure = df['exposure'].values
reach = df['reach'].values
like = df['like'].values
comment = df['comment'].values

df_exp = DataFrame(exposure)
df_rea = DataFrame(reach)
df_like = DataFrame(like)
df_comm = DataFrame(comment)





def prediction(dataframe,days_in,day_out,values):
    raw = []
    for i in range(days_in, 0 ,-1):
        raw.append(dataframe.shift(i))
    for j in range(0,day_out):
        raw.append(dataframe.shift(-j))
    print(raw)
    sum = concat(raw,axis=1)
    sum.dropna(inplace=True)

    train = sum.values
    trainX, trainy = train[:,:-1], train[:,-1]



    model = XGBRegressor(objective='reg:squarederror',n_estimators=80)
    model.fit(trainX,trainy)

    data_in = values[-(days_in):]

    result = model.predict([data_in])


    # print(' Predicted: %.3f' %(result[0]))

    raw.clear()

    return result[0]







print("노출 예상:",prediction(df_exp,days_in,day_out,exposure))
print("도달 예상:",prediction(df_rea,days_in,day_out,reach))
print("공감 에상:",prediction(df_like,days_in,day_out,like))
print("댓글 예상:",prediction(df_comm,days_in,day_out,comment))



