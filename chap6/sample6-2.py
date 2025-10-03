s='HelloWorld'
new_s=s.replace('o','你好',1)
print(new_s)

print(s.center(20))
print(s.center(20,'*'))

s='     Hello     World     '
print(s.strip())
print(s.lstrip())
print(s.rstrip())

s3='ddddllll-Helloworld'
print(s3.strip('ld'))
print(s3.lstrip('ld'))
print(s3.rstrip('dl'))

s4='Hello'
s5='World'
print(s4.join(s5))