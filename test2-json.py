import requests
import json
from bs4 import BeautifulSoup

def pachong(page):
    url = "http://www.4399dmw.com/search/dh-1-0-0-0-0-{}-0/".format(page)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"

    }
    resp = requests.get(url=url, headers=headers)
    html_doc = resp.content.decode("utf-8")

    # 使用bs处理页面源代码
    soup = BeautifulSoup(html_doc)

    list = soup.find('div', class_='lst').find_all('a', class_='u-card')
    for item in list:
        # 取出list中的每一项细节
        mingzi = item.find('p', class_='u-tt').text
        # 图片地址
        pic_url = item.find('img').get('data-src')
        print(mingzi + "-----" + pic_url)

    pass

def main():
    """
    for i in range(14):
        print("爬虫到了第"+str(i)+ "页")
        pachong(i)
    """

    url = "http://www.4399dmw.com/huoying/donghua/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"

    }
    resp = requests.get(url=url, headers=headers)
    html_doc = resp.content.decode("utf-8")

    # 使用bs处理页面源代码
    soup = BeautifulSoup(html_doc)
    list = soup.find_all('div',class_='works__info')[3].find_all('a')
    for item in list:
        print(item.get_text())


    pass

if __name__ == '__main__':
    main()