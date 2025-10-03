for i in 'hello':
    print(i)

for i in range(1,11):
    #print(i)
    if i%2==0:
        print(i,'is even')

s=0
for i in range(1,11):
    s+=i

print('sum of 1-10 is:',s)

for i in range(100,1000):
    sd=i%10
    tens=i//10%10
    hundred=i//100
    if sd**3+tens**3+hundred**3==i:
        print(i)
