s1='HelloWorld'
s2=s1.lower()
print(s1,s2)

s3=s1.upper()
print(s3)

e_mail='ysj@126.com'
lst=e_mail.split('@')
print('mail box name:',lst[0],', mail domain name:',lst[1])

print(s1.count('o'))

print(s1.find('o'))
print(s1.find('p'))

print(s1.index('o'))
#print(s1.index('p'))

print(s1.startswith('H'))
print(s1.startswith('P'))

print('demo.py'.endswith('.py'))
print('text.txt'.endswith('.txt'))
