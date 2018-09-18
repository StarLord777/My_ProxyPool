#代理ip3366
import requests,re,time
from redis import Redis
redis = Redis(db=7)
import getAproxyip

def craw_ip3366():
    #首先获取首页的
    url = 'http://www.ip3366.net/?stype=1&page={}'
    for i in range(1,11):
        r = requests.get(url.format(i),proxies=getAproxyip.returnproxy(),timeout=15).text
        ips = re.findall('tr.*?td>(.*?)</td.*?td>(.*?)</td',r,re.S)
        print(ips)
        for i in ips:
            ip = ':'.join(i)
            print(ip)
            redis.rpush('nowashhttp', ip)
    #然后获取免费页面的四个板块，每个七页
    urls = 'http://www.ip3366.net/free/?stype={}&page={}'
    for i in range(1,5):
        for j in range(1,8):
            url = urls.format(i,j)
            r = requests.get(url,proxies=getAproxyip.returnproxy(),timeout=15).text
            ips = re.findall('tr.*?td>(.*?)</td.*?td>(.*?)</td', r, re.S)
            print(ips)
            for i in ips:
                ip = ':'.join(i)
                redis.rpush('nowashhttp', ip)
            print('*'*80)




craw_ip3366()


