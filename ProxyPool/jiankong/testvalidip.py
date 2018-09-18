#定时检测可用代理池内代理是否可用，如果不可用，则删除
from redis import Redis
import requests,threading,time
redis = Redis(db=7)

def test():
    def wash(value):
        i = str(value)[2:-1]
        proxies = {'http': 'http://' + i,
                   'https': 'https://' + i}
        test_url = 'https://www.baidu.com/'
        try:
            r = requests.get(test_url, proxies=proxies, timeout=15)
            if r.status_code == 200:
                print(i + '可用'+'---可用代理数--{}'.format(redis.scard('validip')))
        except:
            print(i, '------------------------------------不可用，删除')
            redis.srem('validip', i)
    while True:
        for value in redis.smembers('validip'):
            threading.Thread(target=wash, args=(value,)).start()
        time.sleep(5)

test()