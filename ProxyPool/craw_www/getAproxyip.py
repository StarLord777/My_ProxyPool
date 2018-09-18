import requests,re

def returnproxy():
    r = requests.get('http://127.0.0.1/random').text
    ip = r[2:-1]
    print('获取到代理IP：',ip)
    proxies = {'http': 'http://' + ip,
               'https': 'https://' + ip}
    return proxies

#returnproxy()