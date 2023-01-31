import pandas as pd  # 存入excel数据
import requests  # 向页面发送请求
from bs4 import BeautifulSoup as bs  # 解析页面
import time

# 目标地址
url = 'https://s.weibo.com/top/summary'
# 请求头
header = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.108 Safari/537.36',
    'Host': 's.weibo.com',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Accept-Language': 'zh-CN,zh;q=0.9,zh-Hans;q=0.8,und;q=0.7',
    'Accept-Encoding': 'gzip, deflate, br',
    # 定期更换Cookie
    'Cookie': '_s_tentry=weibo.com; Apache=4108659841424.8687.1651678098967; SINAGLOBAL=4108659841424.8687.1651678098967; ULV=1651678099150:1:1:1:4108659841424.8687.1651678098967:; login_sid_t=7c18327dcdc30f319ef1c57154d8bbbb; cross_origin_proto=SSL; SCF=AkMNs7ZXJg-wgfzSCW47uynBXm4rwzKkIFvyZxiYGdscjMQdZrzRdCtYBBfYNob1MQjFWf5laC4EPhkdrpP5Jhc.; UOR=,,blog.csdn.net; SUBP=0033WrSXqPxfM72wWs9jqgMF55529P9D9WFJRTgSbAcU.WlWqG0bY9f85JpVF020e0-NeK271Ke7; SUB=_2AkMU_niZdcPxrAVWm_4RyW_maoxH-jynKxFvAn7uJhMyAxh77kYOqSVutBF-XDR3iBoi8Qk-cQIR-NGq1h6SNuv4'}

# print(rank)
# print(content)
# print(href)


while 1:
    if time.strftime("%M%S") == "0030":
        sheet_name = time.strftime("%Y-%m-%d %H-%M")
        print("hot_search of "+sheet_name+" is collecting...")
        r = requests.get(url, headers=header)  # 发送请求
        soup = bs(r.text, 'html.parser')
        # print(soup)
        rank = []
        content = []
        href = []

        items1 = soup.findAll('td', {"class": "td-01"})
        for each_item in items1:
            rank.append(each_item.text)

        items2 = soup.findAll('td', {"class": "td-02"})
        for each_item in items2:
            for a in each_item.find_all('a'):
                content.append(a.text)
                href.append('https://s.weibo.com' + a.get('href'))
        # print(rank)
        # print(content)
        # print(href)
        df = pd.DataFrame(  # 拼装爬取到的数据为DataFrame
            {
                '热搜排名': rank,
                '热搜标题': content,
                '链接地址': href
            }
        )
        writer = pd.ExcelWriter(sheet_name+".xlsx")
        df.to_excel(writer,index=False)  # 保存结果数据
        # print(time.strftime("%M%S"))
        print("done!")
        time.sleep(3599)