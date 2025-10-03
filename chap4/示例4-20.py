s=0
i=0
while i<=100:
    if i%2==1:
        i+=1
        continue
    s+=i
    i+=1
print('sum of even numbers between 1 and 100 is',s)