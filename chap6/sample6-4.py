s='helloworld'
print('{0:*<20}'.format(s))
print('{0:*>20}'.format(s))
print('{0:*^20}'.format(s))

print(s.center(20,'*'))

print('{0:,}'.format(987654321))
print('{0:,}'.format(987654321.7865))

print('{0:.3f}'.format(3.1415926))
print('{0:.5}'.format('helloworld'))

a=425
print('bin:{0:b}, dec:{0:d}, oct:{0:o}, hex:{0:x}, hex:{0:X}'.format(a))

b=31.415926
print('{0:.2f},{0:.2E},{0:.3e},{0:.3%}'.format(b))