s=0
i=1
while i<11:
    s+=i
    if s>20:
        print('curren value of sum greater than 20 is', i)
        break
    i+=1

print('-'*20)
i=0
while i<3:
    user_name=input('please input your name:')
    pwd=input('please input your password:')
    if user_name=='ysj' and pwd=='888888':
        print('logging in, please wait...')
        break
    else:
        if i<2:
            print('invalid name or password, you have',2-i,'more chances')
    i+=1
else:
    print('you have failed all 3 times!')
