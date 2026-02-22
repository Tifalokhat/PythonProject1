def lower_upper(x):
    lst=[]
    i=ord('a')-ord('A')
    for item in x:
        if 'A'<=item<='Z':
            lst.append(chr(ord(item)+i))
        elif 'a'<=item<='z':
            lst.append(chr(ord(item)-i))
        else:
            lst.append(item)
    return ''.join(lst)
s=input('请输入一个字符串：')
new_s=lower_upper(s)
print(new_s)