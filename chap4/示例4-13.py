i=0
while i<3:
    user_name=input('enter your name:')
    pwd=input('enter your password:')
    if user_name=='ysj' and pwd=='888888':
        print('logging on...please wait')
        i=8
    else:
        if i<2:
            print('invalid user name or password, you have',2-i,'more chances')
        i+=1

if i==3:
    print('sorry, failed to log in')