lst=[]
for i in range(5):
    goods=input('please input the good:')
    lst.append(goods)

for item in lst:
    print(item)

cart=[]
while True:
    flag=False
    num=input('please input the number:')
    for item in lst:
        if item[0:4]==num:
            flag=True
            cart.append(item)
            print('good is added to cart successfully')
            break
    if not flag and num!='q':
        print('good not exists')
    if num=='q':
        break
print('-'*50)
print('the goos in cart are:')
cart.reverse()
for item in cart:
    print(item)