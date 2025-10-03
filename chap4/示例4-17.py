row=eval(input('please input the number of rows:'))
while row%2==0:
    print('please input the number again')
    row=eval(input('please input the number of rows:'))

half_row=(row+1)//2
for i in range(1,half_row+1):
    for j in range(1,half_row-i+1):
        print(' ',end='')
    for j in range(1,i*2):
        if j==1 or j==i*2-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()
for i in range(1, half_row):
    for j in range(1,i+1):
        print(' ',end='')
    for j in range(1,2*(half_row-i)):
        if j==1 or j==2*(half_row-i)-1:
            print('*',end='')
        else:
            print(' ',end='')
    print()