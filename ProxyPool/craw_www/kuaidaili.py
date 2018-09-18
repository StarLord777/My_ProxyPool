import requests,re
from redis import Redis
redis = Redis(db=7)
import getAproxyip


def get_kuaidaili():
    url = 'https://www.kuaidaili.com/free/inha/{}/'
    headers = {
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        'Cookie':'BAIDUID=DC57C1B003EA43B97F7C96C8DDBB0815:FG=1; PSTM=1531885817; BIDUPSID=33E597064BC6A4F0BA3E7C8B61C3694F; HMACCOUN'
                 'T=8A5FC22384F84143; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; PSINO=1; HMVT=6bcd52f51e9b3dce32bec4a3997715ac|153726297'
                 '8|; H_PS_PSSID=1453_21081_22159',
        'Host':'hm.baidu.com',
        'Accept':'image/webp,image/apng,image/*,*/*;q=0.8',
        'Referer':'https://www.kuaidaili.com/free/inha/1/'
    }
    for i in range(1,500):
        realurl = url.format(i)
        print(realurl)
        try:
            r = requests.get(realurl, headers=headers, proxies=getAproxyip.returnproxy()).text
        except:
            pass
        ips = re.findall('IP">(.*?)<',r,re.S)
        ports = re.findall('PORT">(.*?)<',r,re.S)
        print(ips,ports)
        for i in range(len(ips)):
            ip = ips[i]+':'+ports[i]
            redis.rpush('nowashhttp', ip)
        print('加入数据库{}条代理'.format(len(ips)))



get_kuaidaili()