# Action1：汽车投诉信息采集：数据源：http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-1.shtml
# 投诉编号，投诉品牌，投诉车系，投诉车型，问题简述，典型问题，投诉时间，投诉状态

import requests
from bs4 import BeautifulSoup
import pandas as pd

def get_page_content(request_url):
    headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.131 Safari/537.36'}
    html = requests.get(request_url, headers=headers, timeout=10)
    content = html.text
    # 通过content创建BeautifulSoup对象
    soup = BeautifulSoup(content, 'html.parser', from_encoding='utf-8')
    return soup

#分析页面投诉信息
def analysis(soup):
    # 创建DataFrame
    df = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
    # 找到完整的投诉信息框
    temp = soup.find('div', class_="tslb_b")

    tr_list = temp.find_all('tr')
    for tr in tr_list:
        td_list=tr.find_all('td')
        if len(td_list) > 0:
            id, brand, car_model, type, desc, problem, datetime, status = td_list[0].text, td_list[1].text, td_list[2].text, td_list[3].text, td_list[4].text, td_list[5].text, td_list[6].text, td_list[7].text

            temp = {}
            temp['id'] = id
            temp['brand'] = brand
            temp['car_model'] = car_model
            temp['type'] = type
            temp['desc'] = desc
            temp['problem'] = problem
            temp['datetime'] = datetime
            temp['status'] = status
            df=df.append(temp,ignore_index=True)
    return df

result = pd.DataFrame(columns=['id', 'brand', 'car_model', 'type', 'desc', 'problem', 'datetime', 'status'])
# 请求URL
base_url = 'http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-'
page_number = 30
for i in range(page_number):
    request_url=base_url+str(i+1)+',shtml'
    soup = get_page_content(request_url)
    df=analysis(soup)
    result =result.append(df)

print(result)
result.to_csv('car_complain.csv', index=False)


