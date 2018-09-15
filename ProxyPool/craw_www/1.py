from redis import Redis
r = Redis(db=7)

a= r.lpop('nowashhttp')
b = str(a)[2:-1]
print(type(b))
print(b)