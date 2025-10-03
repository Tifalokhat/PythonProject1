number=eval(input('please input 6 digits number:'))
if number==987654:
    print('congratulations! you won a prize!')
else:
    print('sorry, you didn\'t win the prize')

n=98
if n%2:
    print(n, 'is odd')

if not n%2:
    print(n, 'is even')

x=input('please input a string:')
if x:
    print('x is not empty')

if not x:
    print('x is empty')

flag=eval(input('please input a boolean value(True or False):'))
if flag:
    print('flag\'s value is True')
if not flag:
    print('flag\'s value is False')

a=10
b=5
if a>b:max=a
print('max is ', max)