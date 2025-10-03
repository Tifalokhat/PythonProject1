lst=[
    ['city','a','b'],
    ['beijing',102,103],
    ['shanghai',104,504],
    ['shenzhen',100,39]
]
print('lst:',lst)

for row in lst:
    for item in row:
        print(item,end='\t')
    print()

lst2=[[j for j in range(5)] for i in range(4)]
print('lst2:',lst2)