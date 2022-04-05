import requests
from lxml import etree

def pachong(url):
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"

    }
    resp = requests.get(url=url, headers=headers)
    # 页面的源码
    html_doc = resp.content.decode("utf-8")
    # 使用etree去转化html_doc，转化为了一个html对象，此时element对象可以使用xpath语法
    html = etree.HTML(html_doc)
    dongmantitle = (html.xpath("//div[@class='u-ct']/p[@class='u-tt']/text()"))
    dongmanpic = (html.xpath("//div[@class='lst']/a[@class='u-card']/img/@data-src"))
    print(dongmantitle)
    print(dongmanpic)

def next_page(url):
    url = url
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"

    }
    resp = requests.get(url=url, headers=headers)
    # 页面的源码
    html_doc = resp.content.decode("utf-8")
    html = etree.HTML(html_doc)
    next_page = html.xpath("//a[contains(text(),'下一页')]/@href")
    really_next_page = "http://www.4399dmw.com" + next_page[0]
    return really_next_page
    pass

def main():
    url = "http://www.4399dmw.com/search/dh-1-0-0-0-0-1-0/"
    while True:
        try:
            print("开始爬行的url："+ url)
            pachong(url)
            url=next_page(url)
        except:
            break

    print("最后一页也爬完了")

    pass

if __name__ == '__main__':
    main()