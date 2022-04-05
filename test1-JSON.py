import requests
import json

def main():
        url = "https://api.help.bj.cn/apis/weather/?id=101060101"
        resp = requests.get(url=url)
        content = resp.content
        print(content)
        shuju = json.loads(content)
        print(shuju)


        pass

if __name__ == '__main__':
    main()