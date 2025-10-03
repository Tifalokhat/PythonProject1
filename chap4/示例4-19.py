for i in 'hello':
    if i=='e':
        break
    print(i)
print('-'*20)
for i in range(3):
    user_name=input('please input your name:')
    pwd=input('please input your password:')
    if user_name == 'ysj' and pwd == '888888':
        print('logging in, please wait...')
        break
    else:
        if i < 2:
            print('invalid name or password, you have',2-i,'more chances')
else:
    print('you have failed all 3 times')
