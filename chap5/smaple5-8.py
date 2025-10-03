lst=[4,56,3,78,40,56,89]
lst.sort()
print('after sorting:',lst)

lst.sort(reverse=True)
print('descending:',lst)

print('-'*50)
lst2=['banana','apple','Cat','Orange']
print('lst2:',lst2)
lst2.sort()
print('ascending:',lst2)
lst2.sort(reverse=True)
print('descending:',lst2)

lst2.sort(key=str.lower)
print('lst2:',lst2)