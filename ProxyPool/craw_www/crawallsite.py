'''
此页面为集成所有代理网站的抓取方法，供集成调用，也可分开调用
收录网站：
西刺代理
ip66
ip3366
快代理
'''
from bs4 import BeautifulSoup
import requests,time
from redis import Redis
redis = Redis(db=7)


class Crawler():
    def __init__(self):
        pass