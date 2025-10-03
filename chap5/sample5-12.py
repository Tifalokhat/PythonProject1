t=('hello',[10,20,30],'python','world')
print(t)

t=tuple('helloworld')
print(t)

t=tuple([10,20,30,40])
print(t)

print('10 in t?', 10 in t)
print('10 not in t?', 10 not in t)
print('max:',max(t))
print('min:',min(t))
print('len:',len(t))
print('t.index:',t.index(10))
print('t.count:',t.count(10))

t=(10)
print(t,type(t))

y=(10,)
print(y,type(y))