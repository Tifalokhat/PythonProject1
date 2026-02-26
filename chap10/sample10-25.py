import jieba
with open('华为笔记本.txt','r',encoding='utf-8') as file:
    s=file.read()
# print(s)
lst=jieba.lcut(s)
# print(lst)

set1=set(lst)
d={}
for item in set1:
    if len(item)>=2:
        d[item]=0
for item in lst:
    if item in d:
        d[item]=d[item]+1
new_lst=[]
for item in d:
    new_lst.append((item,d[item]))
# print(new_lst)

new_lst.sort(key=lambda x:x[1],reverse=True)
print(new_lst[0:11])