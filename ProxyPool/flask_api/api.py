from flask import Flask
from redis import Redis
r = Redis(db=7)


__all__ = ['app']
app = Flask(__name__)

@app.route('/')
def index():
    return '<h2>欢迎使用代理池</h2>'

@app.route('/random')
def random():
    ip = r.srandmember('validip',1)[0]
    return ip

@app.route('/count')
def count():
    str = '<h2>剩余代理总数：{}</h2>'.format(r.scard('validip'))
    return str

if __name__ == '__main__':
    app.run()

