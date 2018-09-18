import requests,threading,time
from redis import Redis
redis = Redis(host='127.0.0.1',db=7)


def wash_ip():
    print('线程{}启动'.format(threading.current_thread().name))
    while redis.llen('nowashhttp')>1:
        i = str(redis.lpop('nowashhttp'))[2:-1]
        print(i)
        proxies = {'http': 'http://' + i,
                   'https': 'https://' + i}
        test_url = 'https://www.baidu.com/'
        try:
            r = requests.get(test_url,proxies=proxies, timeout=15)
            if r.status_code == 200:
                print(i + '可用')
                redis.sadd('validip',i)
        except:
            pass

if __name__ == '__main__':
    for i in range(500):
        threading.Thread(target=wash_ip).start()