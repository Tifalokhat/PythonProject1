import re
pattern='\\d\\.\\d+'
s='I study Python 3.11 every day'
match=re.match(pattern,s,re.I)
print(match)
s2='3.11Python I study every day'
match2=re.match(pattern,s2)
print(match2)

print('start position:',match2.start())
print('end position:', match2.end())
print('position range:',match2.span())
print('String to be matched:',match2.string)
print('matched data:',match2.group())