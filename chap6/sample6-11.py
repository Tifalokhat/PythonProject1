import re
pattern='\\d\\.\\d+'
s='I study Python3.11 every day Python2.7 I love you'
s2='4.10 Python I study every day'
s3='I study Python every day'
match=re.findall(pattern,s)
match2=re.findall(pattern,s2)
match3=re.findall(pattern,s3)

print(match)
print(match2)
print(match3)