answer=input('Did you drink?')
if answer=='y':
    proof=eval(input('please input the percentage of alcohol:'))
    if proof<20:
        print('not valid for drunk driving')
    elif proof<80:
        print('valid for dunk driving. stop driving')
    else:
        print('serious dunk driving. please stop driving immediately.')
else:
    print('it\'s ok')