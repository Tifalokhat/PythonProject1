s='helloworldhelloworldadfdfdeoodllffe'
s1=''
for item in s:
    if item not in s1:
        s1+=item
print(s1)

s2=''
for i in range(len(s)):
    if s[i] not in s2:
        s2+=s[i]
print(s2)

s3=set(s)
lst=list(s3)
lst.sort(key=s.index)
print(''.join(lst))