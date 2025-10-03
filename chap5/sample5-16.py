d={'hello':10,'world':20,'python':30}
print(d['hello'])
print(d.get('hello'))

# print(d['java'])
print(d.get('java'))
print(d.get('java','not exist!'))

for item in d.items():
    print(item)

for a,b in d.items():
    print(a,'---->',b)