import requests

def main():
    url = "http://www.4399dmw.com/donghua/"
    headers = {
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    #代理
    proxies = {"HTTP":"175.174.190.164:8080"}


    urla = url.format("1")
    print(urla)
    resp = requests.get(url=urla,headers=headers,proxies=proxies)
    with open("a.txt","wb+") as f:
        #写入文件
        f.write(resp.content)

    pass


if __name__ == '__main__':
    main()
