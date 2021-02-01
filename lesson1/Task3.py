import pandas as pd
import numpy as np

df=pd.read_csv('./data/car_complain.csv')

df=df.drop('problem',axis=1).join(df.problem.str.get_dummies(','))

def f(x):
    x=x.replace('一汽-大众','一汽大众')
    return x

df['brand']=df['brand'].apply(f)
result=df.groupby(['brand'])['id'].agg(['count'])

tags=df.columns[7:]
result2=df.groupby(['brand'])[tags].agg(['sum'])

result2=result.merge(result2,left_index=True,right_index=True,how='left')

result2.reset_index(inplace=True)

result2.to_csv('./data/result.csv')

#品牌投诉总数
result2=result2.sort_values('count',ascending=False)
print(result2)

#车型投诉总数
result3=df.groupby(['car_model'])['id'].agg(['count'])
result3.reset_index(inplace=True)
result3=result3.sort_values('count',ascending=False)
print(result3)

#品牌的平均车型投诉
result4=df.groupby(['brand','car_model'])['id'].agg(['count'])
print(result4)