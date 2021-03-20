from _ast import Lambda

import pandas as pd

from nltk.tokenize import word_tokenize

pd.set_option('max_columns',None)
#数据加载
dataset = pd.read_csv('./Market_Basket_Optimisation.csv',header = None)
print(dataset)
print(dataset.shape)

transactions = []
item_count = {}
#按行进行遍历
for i in range(dataset.shape[0]):
    temp = []
    #按照列进行遍历
    for j in range(dataset.shape[1]):
        item = str(dataset.values[i,j])
        if item != 'nan':
            temp.append(item)
            if item not in item_count:
                item_count[item] = 1
            else:
                item_count[item] += 1
    transactions.append(temp)
print(transactions)

from wordcloud import WordCloud
def create_word_cloud(f):
	cut_text = word_tokenize(f)
	cut_text = " ".join(cut_text)
	wc = WordCloud(
		max_words=100,
		width=2000,
		height=1200,
    )
	wordcloud = wc.generate(cut_text)
	wordcloud.to_file("wordcloud.jpg")

all_word = ' '.join('%s' %item for item in transactions)
create_word_cloud(all_word)

#Top10的商品有哪些
print(sorted(item_count.items(), key=Lambda x:x[1], reverse=True)[:10])