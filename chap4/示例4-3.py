number=eval(input('please input your number:'))
if number==987654:
    print('Congratulations!')
else:
    print('Sorry!')

result='Congratulations!' if number==987654 else 'Sorry!'
print(result)

print('Congratulations!' if number==987654 else 'Sorry!')