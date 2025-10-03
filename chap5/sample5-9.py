lst=[4,56,3,78,40,56,89]
print('lst:',lst)

asc_lst=sorted(lst)
print('asc_lst:',asc_lst,id(asc_lst))
print('lst:',lst,id(lst))

desc_lst=sorted(lst,reverse=True)
print('desc_lst:',desc_lst,id(desc_lst))
print('lst:',lst,id(lst))

lst2=['banana','apple','Cat','Orange']
print('lst2:',lst2,id(lst2))

new_lst2=sorted(lst2,key=str.lower)
print('new_lst2:',new_lst2,id(new_lst2))
print('lst2:',lst2,id(lst2))