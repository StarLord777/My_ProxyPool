#定时检测可用代理池内代理是否可用，如果不可用，则删除
from redis import Redis
import requests,threading
redis = Redis(db=7)

def test():
    def wash(value):
        i = str(value)[2:-1]
        proxies = {'http': 'http://' + i,
                   'https': 'https://' + i}
        test_url = 'https://www.google.com/?hl=zh_cn'
        try:
            r = requests.get(test_url, proxies=proxies, timeout=15)
            if r.status_code == 200:
                print(i + '可用')
                redis.sadd('googlehttp',i)
        except:
            print('no')
    for value in redis.smembers('validip'):
        threading.Thread(target=wash,args=(value,)).start()



test()

