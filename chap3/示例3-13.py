x=10
y=3
z=x/y
print(z,type(z))

print('float类型转为int类型：',int(3.14))
print('float类型转为int类型：',int(3.9))
print('float类型转为int类型：',int(-3.14))
print('float类型转为int类型：',int(-3.9))

print('将int转为float类型：',float(10))
print(int('100')+int('200'))
print('100'+'200')
#print(int('3.14')) error

print(ord('杨'))
print(chr(26472))

print('十进制转成十六进制：',hex(26472))
print('十进制转成八进制：',oct(26472))
print('十进制转成二进制：',bin(26472))