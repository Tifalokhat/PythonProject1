import random
rand=random.randint(1,100)
count=1
while count<=10:
    number=eval(input('please guess the number(1-100):'))
    if number==rand:
        print('right')
        break
    elif number>rand:
        print('big')
    else:
        print('small')
    count+=1
if count<=3:
    print('smart! you guess',count,'times')
elif count<=6:
    print('just so so. you guess',count,'times')
else:
    print('too many times. you guess',count,'times')