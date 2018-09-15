from bs4 import BeautifulSoup
import requests,time
from redis import Redis
redis = Redis(db=7)

def craw_xici():
    ip_list = []  # 存储爬下来的IP地址和端口
    url = 'http://www.xicidaili.com/wt/'
    url1 = 'http://www.xicidaili.com/wn/'
    url2 = 'http://www.xicidaili.com/nn/'
    url3 = 'http://www.xicidaili.com/nt/'
    headers = {  # 创建字典，存储自己浏览器上的信息，从而模拟浏览
        'Cookie': '_free_proxy_session=BAh7B0kiD3Nlc3Npb25faWQGOgZFVEki'
                  'JWIzYzA0ZWNhN2U4YmJiZmI3N2M1YzQ0ZmFjZDU1OGFhBjsAVEkiE'
                  'F9jc3JmX3Rva2VuBjsARkkiMXhOSktRWmRoaGlLRXd0UnU1NmtDWT'
                  'FvVzh6SVFZUWxTWnlLeGVIVVVpNEU9BjsARg%3D%3D--f0f7b59b27'
                  'a7bbb3e87c4eb1f5043c9c5f5ef435; __guid=264997385.176939'
                  '6082676313900.1532227595275.8433; Hm_lvt_0cf76c77469e965'
                  'd2957f0553e6ecf59=1532227595; monitor_count=5; Hm_lpvt_0'
                  'cf76c77469e965d2957f0553e6ecf59=1532227642',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKi'
                      't/537.36 (KHTML, like Gecko) Chrome/49.0.2623.22'
                      '1 Safari/537.36 SE 2.X MetaSr 1.0'
    }
    #得到一页的IP，并存储至ip_list
    def get_one_page(url):
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'lxml')
        ips = soup.select('table tr')
        ips.remove(ips[0])
        for i in ips:
            for j, k in enumerate(i):
                if j == 3:
                    port = k.find_next_sibling().get_text()
                    ip = k.get_text()
                    ip_list.append(ip + ':' + port)
    # 得到20页的IP
    def get_all_pages(url):
        for i in range(1, 20):
            url_ = url + str(i)
            get_one_page(url_)
    #得到四个类目每个类目前20页代理
    get_all_pages(url)
    get_all_pages(url1)
    get_all_pages(url2)
    get_all_pages(url3)
    print(len(ip_list))
    print(ip_list)
    for i in ip_list:
        redis.rpush('nowashhttp', i)

craw_xici()

