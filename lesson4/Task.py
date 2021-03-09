import pandas as pd

pd.set_option('max_columns',None)
#数据加载
dataset = pd.read_csv('./Market_Basket_Optimisation.csv',header = None)
print(dataset)
print(dataset.shape)

transactions = []
#按行进行遍历
for i in range(0,dataset.shape[0]):
    temp = []
    #按照列进行遍历
    for j in range(0,dataset.shape[1]):
        if str(dataset.values[i,j]) != 'nan':
            temp.append(dataset.values[i,j])
    transactions.append(temp)

from efficient_apriori import apriori
itemsets, rules = apriori(transactions, min_support=0.02,  min_confidence=0.2)
print("频繁项集：", itemsets)
print("关联规则：", rules)
