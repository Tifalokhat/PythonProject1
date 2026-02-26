class Student:
    school='北京XXX教育'

    def __init__(self,name,age):
        self.name=name
        self.age=age

    def show(self):
        print(f'我叫{self.name}，今年{self.age}岁了')

stu=Student('ysj',18)
stu2=Student('陈梅梅',20)
stu3=Student('马丽',21)
stu4=Student('Marry',22)

print(type(stu))
print(type(stu2))
print(type(stu3))
print(type(stu4))

Student.school='派森教育'

lst=[stu,stu2,stu3,stu4]
for item in lst:
    item.show()