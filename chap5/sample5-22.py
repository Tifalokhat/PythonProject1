data=eval(input('please input the data:'))
match data:
    case {'name':'ysj','age':20}:
        print('dictionary')
    case [10,20,30]:
        print('list')
    case (10,20,40):
        print('tuple')
    case _:
        print('else...')