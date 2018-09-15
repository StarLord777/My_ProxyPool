#代理66
import requests,re
from redis import Redis
redis = Redis(db=7)

def craw_66ip():
    url = 'http://www.66ip.cn/{}.html'
    for i in range(1,1300):
        r = requests.get(url.format(i)).text
        ips = re.findall('td>(\w+\.\w+\.\w+\.\w+)</td',r,re.S)
        ports = re.findall('\.\w+</td.*?>(\w+)</td',r,re.S)
        for i in range(len(ips)):
            str = ips[i]+":"+ports[i]
            redis.rpush('nowashhttp',str)
            print('加入')


craw_66ip()



