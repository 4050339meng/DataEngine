import pandas as pd

#数据预处理
train = pd.read_csv('./train.csv')

train['Datetime'] = pd.to_datetime(train['Datetime'])
train.index = train['Datetime']

train.drop(['ID','Datetime'], axis=1, inplace=True)

daily_train = train.resample('D').sum()

daily_train['ds'] =daily_train.index
daily_train['y'] = daily_train['Count']
daily_train.drop(['Count'], axis=1, inplace=True)

#预测接下来 7 个月的乘客数量

from fbprophet import Prophet
m = Prophet(yearly_seasonality=True, seasonality_prior_scale=0.1)
m.fit(daily_train)
# 预测未来7个月，213天
future = m.make_future_dataframe(periods=213)
forecast = m.predict(future)
print(forecast)
m.plot(forecast)
