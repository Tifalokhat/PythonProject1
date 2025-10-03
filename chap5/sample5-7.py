lst=['hello','world','python']
print(lst)
print('list:',lst,id(lst))
lst.append('sql')
print('after append:',lst,id(lst))

lst.insert(1,100)
print(lst)

lst.remove('world')
print('after remove:',lst,id(lst))

print(lst.pop(1))
print('after pop:',lst,id(lst))

# lst.clear()
# print(lst,id(lst))

lst.reverse()
print(lst)

new_lst=lst.copy()
print(lst,id(lst))
print(new_lst,id(new_lst))

lst[1]='mysql'
print(lst)
print(new_lst)