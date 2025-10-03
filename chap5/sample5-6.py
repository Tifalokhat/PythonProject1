lst=['hello','world','python','php']
for item in lst:
    print(item)
print('-'*50)
for i in range(0,len(lst)):
    print(lst[i])
print('-'*50)
for index,item in enumerate(lst):
    print(index,item)
for index,item in enumerate(lst,start=1):
    print(index,item)