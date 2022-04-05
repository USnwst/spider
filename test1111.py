import socket

from whois import whois

def main():
    data = whois.whois('www.baidu.com')
    print(data)
    pass

if __name__ == '__main__':
    main()