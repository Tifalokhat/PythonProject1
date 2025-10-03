d={1001:'limei',1002:'wanghua',1003:'zhangfeng'}
print(d)

d[1004]='zhanglili'
print(d)

keys=d.keys()
print(keys)
print(list(keys))
print(tuple(keys))

values=d.values()
print(values)
print(list(values))
print(tuple(values))

lst=list(d.items())
print(lst)

d=dict(lst)
print(d)

print(d.pop(1001))
print(d)

print(d.pop(1008,'not exist'))

print(d.popitem())
print(d)

d.clear()
print(d)

print(bool(d))